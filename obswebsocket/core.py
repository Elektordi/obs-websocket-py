import base64
import hashlib
import json
import logging
import socket
import threading
import websocket
import time

from . import exceptions
from . import base_classes
from . import events

LOG = logging.getLogger(__name__)


class obsws:
    """
    Core class for using obs-websocket-py

    Simple usage: (v5 api)
        >>> from obswebsocket import obsws, requests
        >>> client = obsws("localhost", 4455, "secret")
        >>> client.connect()
        >>> client.call(requests.GetVersion()).getObsVersion()
        '29.0.0'
        >>> client.disconnect()

    Legacy usage: (v4 api)
        >>> from obswebsocket import obsws, requests
        >>> client = obsws("localhost", 4444, "secret", legacy=True)
        >>> client.connect()
        >>> client.call(requests.GetVersion()).getObsStudioVersion()
        '25.0.0'
        >>> client.disconnect()

    For advanced usage, including events callback, see the 'samples' directory.
    """

    def __init__(self, host='localhost', port=4444, password='', legacy=None, timeout=60, authreconnect=0, on_connect=None, on_disconnect=None):
        """
        Construct a new obsws wrapper

        :param host: Hostname to connect to
        :param port: TCP Port to connect to (Default is 4444)
        :param password: Password for the websocket server (Leave this field empty if auth is not enabled)
        :param legacy: Server is using old obs-websocket protocol (v4). Default is v5 (False) except if port is 4444.
        :param timeout: How much seconds to wait for an answer after sending a request.
        :param authreconnect: Try to reconnect if websocket is closed, value is number of seconds between attemps.
        :param on_connect: Function to call after successful connect, with parameter (obsws)
        :param on_disconnect: Function to call after successful disconnect, with parameter (obsws)
        """
        self.host = host
        self.port = port
        self.password = password
        self.legacy = legacy
        self.timeout = timeout
        self.authreconnect = authreconnect
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect

        if self.legacy is None:
            self.legacy = (self.port == 4444)

        self.id = 1
        self.thread_recv = None
        self.thread_reco = None
        self.ws = None
        self.eventmanager = EventManager()
        self.events = {}
        self.answers = {}
        self.server_version = None

    def connect(self):
        """
        Connect to the websocket server

        :return: Nothing
        """
        try:
            self.ws = websocket.WebSocket()
            url = "ws://{}:{}".format(self.host, self.port)
            LOG.info("Connecting to %s..." % (url))
            self.ws.connect(url)
            LOG.info("Connected!")
            if self.legacy:
                self._auth_legacy()
            else:
                self._auth()

            if self.thread_recv is not None:
                self.thread_recv.running = False
            self.thread_recv = RecvThread(self)
            self.thread_recv.daemon = True
            self.thread_recv.start()
            if self.on_connect:
                self.on_connect(self)
        except socket.error as e:
            if self.authreconnect:
                if not self.thread_reco:
                    LOG.warning("Connection failed, reconnecting in %s second(s)." % (self.authreconnect))
                    self.thread_reco = ReconnectThread(self)
                    self.thread_reco.daemon = True
                    self.thread_reco.start()
                else:
                    LOG.warning("Connection failed, but reconnect timer already running.")
            else:
                raise exceptions.ConnectionFailure(str(e))

    def reconnect(self):
        """
        Restart the connection to the websocket server

        :return: Nothing
        """
        self.disconnect()
        self.connect()

    def disconnect(self):
        """
        Disconnect from websocket server

        :return: Nothing
        """
        if self.thread_recv and self.thread_recv.running:
            if self.on_disconnect:
                self.on_disconnect(self)
            self.thread_recv.running = False
        if not self.ws.connected:
            return
        LOG.info("Disconnecting...")
        try:
            self.ws.close()
        except socket.error:
            pass
        self.thread_recv.join()
        self.thread_recv = None

    def _auth(self):
        message = self.ws.recv()
        LOG.debug("Got Hello message: {}".format(message))
        result = json.loads(message)

        if result.get('op') != 0:
            raise exceptions.ConnectionFailure(result.get('error', "Invalid Hello message."))
        self.server_version = result['d'].get('obsWebSocketVersion')

        if result['d'].get('authentication'):
            auth = self._build_auth_string(result['d']['authentication']['salt'], result['d']['authentication']['challenge'])
        else:
            auth = ''

        payload = {
            "op": 1,
            "d": {
                "rpcVersion": 1,
                "authentication": auth,
                "eventSubscriptions": 1023  # EventSubscription::All
            }
        }
        LOG.debug("Sending Identify message: {}".format(json.dumps(payload)))
        self.ws.send(json.dumps(payload))

        message = self.ws.recv()
        if not message:
            raise exceptions.ConnectionFailure("Empty response to Identify, password may be inconnect.")
        LOG.debug("Got Identified message: {}".format(message))
        result = json.loads(message)
        if result.get('op') != 2:
            raise exceptions.ConnectionFailure(result.get('error', "Invalid Identified message."))
        if result['d'].get('negotiatedRpcVersion') != 1:
            raise exceptions.ConnectionFailure(result.get('error', "Invalid RPC version negotiated."))

    def _auth_legacy(self):
        auth_payload = json.dumps({
            "request-type": "GetAuthRequired",
            "message-id": str(self.id),
        })
        LOG.debug("Sending initial message: {}".format(auth_payload))
        self.id += 1
        self.ws.send(auth_payload)
        message = self.ws.recv()
        LOG.debug("Got initial response: {}".format(message))
        result = json.loads(message)

        if result.get('status') != 'ok':
            raise exceptions.ConnectionFailure(result.get('error', "Invalid initial response."))

        if result.get('authRequired'):
            auth = self._build_auth_string(result['salt'], result['challenge'])
            auth_payload = json.dumps({
                "request-type": "Authenticate",
                "message-id": str(self.id),
                "auth": auth,
            })
            LOG.debug("Sending auth message: {}".format(auth_payload))
            self.id += 1
            self.ws.send(auth_payload)
            message = self.ws.recv()
            LOG.debug("Got auth response: {}".format(message))
            result = json.loads(message)
            if result.get('status') != 'ok':
                raise exceptions.ConnectionFailure(result.get('error', "Invalid auth response."))
        pass

    def _build_auth_string(self, salt, challenge):
        secret = base64.b64encode(
            hashlib.sha256(
                (self.password + salt).encode('utf-8')
            ).digest()
        )
        auth = base64.b64encode(
            hashlib.sha256(
                secret + challenge.encode('utf-8')
            ).digest()
        ).decode('utf-8')
        return auth

    def call(self, obj):
        """
        Make a call to the OBS server through the Websocket.

        :param obj: Request (class from obswebsocket.requests module) to send
            to the server.
        :return: Request object populated with response data.
        """
        if not isinstance(obj, base_classes.Baserequests):
            raise exceptions.ObjectError("Call parameter is not a request object")
        data = obj.data()

        message_id = str(self.id)
        self.id += 1
        event = threading.Event()
        self.events[message_id] = event

        if self.legacy:
            payload = {
                "message-id": message_id,
                "request-type": obj.name
            }
            payload.update(data)
        else:
            payload = {
                "op": 6,
                "d": {
                    "requestId": message_id,
                    "requestType": obj.name,
                    "requestData": data
                }
            }
        LOG.debug("Sending message id {}: {}".format(message_id, json.dumps(payload)))
        self.ws.send(json.dumps(payload))

        event.wait(self.timeout)
        self.events.pop(message_id)

        if message_id in self.answers:
            r = self.answers.pop(message_id)
            if self.legacy:
                obj.input(r, r['status'] == 'ok')
            else:
                obj.input(r.get('responseData', {}), r['requestStatus']['result'])
            return obj
        raise exceptions.MessageTimeout("No answer for message {}".format(message_id))

    def register(self, func, event=None):
        """
        Register a new hook in the websocket client

        :param func: Callback function pointer for the hook
        :param event: Event (class from obswebsocket.events module) to trigger
            the hook on. Default is None, which means trigger on all events.
        :return: Nothing
        """
        self.eventmanager.register(func, event)

    def unregister(self, func, event=None):
        """
        Unregister a new hook in the websocket client

        :param func: Callback function pointer for the hook
        :param event: Event (class from obswebsocket.events module) which
            triggered the hook on. Default is None, which means unregister this
            function for all events.
        :return: Nothing
        """
        self.eventmanager.unregister(func, event)


class RecvThread(threading.Thread):

    def __init__(self, core):
        self.core = core
        self.ws = core.ws
        self.running = True
        threading.Thread.__init__(self)

    def run(self):
        while self.running:
            message = ""
            try:
                message = self.ws.recv()

                # recv() can return an empty string (Issue #6)
                if not message:
                    continue

                result = json.loads(message)
                if self.core.legacy:
                    if 'update-type' in result:
                        LOG.debug("Got event: {}".format(result))
                        obj = self.build_event(result)
                        self.core.eventmanager.trigger(obj)
                    elif 'message-id' in result:
                        LOG.debug("Got answer for id {}: {}".format(result['message-id'], result))
                        if result['message-id'] in self.core.events:
                            self.core.answers[result['message-id']] = result
                            self.core.events[result['message-id']].set()
                        else:
                            LOG.warning("Drop message with unknow message-id: {}".format(result))
                    else:
                        LOG.warning("Unknown message: {}".format(result))
                else:
                    if result['op'] == 5:  # Event
                        LOG.debug("Got event: {}".format(result))
                        obj = self.build_event(result['d'])
                        self.core.eventmanager.trigger(obj)
                    elif result['op'] == 7:  # RequestResponse
                        LOG.debug("Got answer for id {}: {}".format(result['d']['requestId'], result))
                        if result['d']['requestId'] in self.core.events:
                            self.core.answers[result['d']['requestId']] = result['d']
                            self.core.events[result['d']['requestId']].set()
                    else:
                        LOG.warning("Unknown message: {}".format(result))

            except websocket.WebSocketConnectionClosedException:
                if self.running:
                    if self.core.authreconnect:
                        LOG.warning("Connection lost, attempting to reconnect...")
                        self.core.reconnect()
                    else:
                        LOG.warning("Connection lost!")
                        self.core.disconnect()
                    break
            except OSError as e:
                if self.running:
                    raise e
            except (ValueError, exceptions.ObjectError) as e:
                LOG.warning("Invalid message: {} ({})".format(message, e))
        # end while
        LOG.debug("RecvThread ended.")

    def build_event(self, data):
        if self.core.legacy:
            name = data["update-type"]
        else:
            name = data["eventType"]
        try:
            obj = getattr(events, name)()
        except AttributeError:
            raise exceptions.ObjectError("Invalid event {}".format(name))
        if self.core.legacy:
            obj.input(data)
        else:
            obj.input(data.get("eventData", {}))
        return obj


class ReconnectThread(threading.Thread):

    def __init__(self, core):
        self.core = core
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.core.authreconnect)
        self.core.thread_reco = None
        self.core.reconnect()


class EventManager:

    def __init__(self):
        self.functions = []

    def register(self, callback, trigger):
        self.functions.append((callback, trigger))

    def unregister(self, callback, trigger):
        for c, t in self.functions:
            if (c == callback) and (trigger is None or t == trigger):
                self.functions.remove((c, t))

    def trigger(self, data):
        for callback, trigger in self.functions:
            if trigger is None or isinstance(data, trigger):
                callback(data)
