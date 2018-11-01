#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import websocket
import json
import hashlib
import base64
import threading
import time

import logging
LOG = logging.getLogger(__name__)

from . import exceptions
from . import base_classes
from . import events

class obsws:
    """
    Core class for using obs-websocket-py

    Simple usage:
        >>> import obswebsocket, obswebsocket.requests
        >>> client = obswebsocket.obsws("localhost", 4444, "secret")
        >>> client.connect()
        >>> client.call(obswebsocket.requests.GetVersion()).getObsWebsocketVersion()
        u'4.1.0'
        >>> client.disconnect()

    For advanced usage, including events callback, see the 'samples' directory.
    """

    def __init__(self, host = 'localhost', port = 4444, password = ''):
        """
        Construct a new obsws wrapper

        :param host: Hostname to connect to
        :param port: TCP Port to connect to (Default is 4444)
        :param password: Password for the websocket server (Leave this field empty if no auth enabled
            on the server)
        """
        self.id = 1
        self.thread_recv = None
        self.eventmanager = EventManager()
        self.answers = {}

        self.host = host
        self.port = port
        self.password = password

    def connect(self, host = None, port = None):
        """
        Connect to the websocket server

        :return: Nothing
        """
        if not host is None:
            self.host = host
        if not port is None:
            self.port = port

        try:
            self.ws = websocket.WebSocket()
            LOG.info("Connecting...")
            self.ws.connect("ws://{}:{}".format(self.host, self.port))
            LOG.info("Connected!")
            self._auth(self.password)
            self._run_threads()
        except socket.error as e:
            raise exceptions.ConnectionFailure(str(e))

    def reconnect(self):
        """
        TODO (Not yet implemented)

        :return: Nothing
        """
        raise exceptions.ConnectionFailure("Reconnect not implemented")

    def disconnect(self):
        """
        Disconnect from websocket server

        :return: Nothing
        """
        LOG.info("Disconnecting...")
        if not self.thread_recv is None:
            self.thread_recv.running = False

        try:
            self.ws.close()
        except socket.error as e:
            pass

        if not self.thread_recv is None:
            self.thread_recv.join()
            self.thread_recv = None

    def _auth(self, password):
        auth_payload = {"request-type": "GetAuthRequired", "message-id": str(self.id)}
        self.id += 1
        self.ws.send(json.dumps(auth_payload))
        result = json.loads(self.ws.recv())

        if result['status'] != 'ok':
            raise exceptions.ConnectionFailure(result['error'])
            
        if result.get('authRequired'):
            secret = base64.b64encode(hashlib.sha256((password + result['salt']).encode('utf-8')).digest())
            auth = base64.b64encode(hashlib.sha256(secret + result['challenge'].encode('utf-8')).digest()).decode('utf-8')

            auth_payload = {"request-type": "Authenticate", "message-id": str(self.id), "auth": auth}
            self.id += 1
            self.ws.send(json.dumps(auth_payload))
            result = json.loads(self.ws.recv())
            if result['status'] != 'ok':
                raise exceptions.ConnectionFailure(result['error'])
        pass

    def _run_threads(self):
        if not self.thread_recv is None:
            self.thread_recv.running = False
        self.thread_recv = RecvThread(self)
        self.thread_recv.daemon = True
        self.thread_recv.start()

    def call(self, obj):
        """
        Make a call to the OBS server through the Websocket.

        :param obj: Request (class from obswebsocket.requests module) to send to the server.
        :return: Request object populated with response data.
        """
        if not isinstance(obj, base_classes.Baserequests):
            raise exceptions.ObjectError("Call parameter is not a request object")
        payload = obj.data()
        r = self.send(payload)
        obj.input(r)
        return obj

    def send(self, data):
        """
        Make a raw json call to the OBS server through the Websocket.

        :param obj: Request (python dict) to send to the server. Do not include field "message-id".
        :return: Response (python dict) from the server.
        """
        id = str(self.id)
        self.id += 1
        data["message-id"] = id
        LOG.debug("Sending message id {}: {}".format(id, data))
        self.ws.send(json.dumps(data))
        return self._waitmessage(id)

    def _waitmessage(self, id):
        timeout = time.time() + 60 # Timeout = 60s
        while time.time() < timeout:
            if id in self.answers:
                return self.answers.pop(id)
            time.sleep(0.1)
        raise exceptions.MessageTimeout("No answer for message {}".format(id))

    def register(self, function, event = None):
        """
        Register a new hook in the websocket client

        :param function: Callback function pointer for the hook
        :param event: Event (class from obswebsocket.events module) to trigger the hook on.
            Default is None, which means trigger on all events.
        :return: Nothing
        """
        self.eventmanager.register(function, event)

    def unregister(self, function, event = None):
        """
        Unregister a new hook in the websocket client

        :param function: Callback function pointer for the hook
        :param event: Event (class from obswebsocket.events module) which triggered the hook on.
            Default is None, which means unregister this function for all events.
        :return: Nothing
        """
        self.eventmanager.unregister(function, event)



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

                # recv() can return empty string if socket is closed during blocking read (Issue #6)
                if not message:
                    continue

                result = json.loads(message)
                if 'update-type' in result:
                    LOG.debug("Got message: {}".format(result))
                    obj = self.buildEvent(result)
                    self.core.eventmanager.trigger(obj)
                elif 'message-id' in result:
                    LOG.debug("Got answer for id {}: {}".format(result['message-id'], result))
                    self.core.answers[result['message-id']] = result
                else:
                    LOG.warning("Unknow message: {}".format(result))
            except websocket.WebSocketConnectionClosedException:
                if self.running:
                    self.core.reconnect()
            except (ValueError, exceptions.ObjectError) as e:
                LOG.warning("Invalid message: {} ({})".format(message, e))
        # end while
        LOG.debug("RecvThread ended.")

    def buildEvent(self, data):
        name = data["update-type"]
        try:
            obj = getattr(events, name)()
        except AttributeError:
            raise exceptions.ObjectError("Invalid event {}".format(name))
        obj.input(data)
        return obj


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
