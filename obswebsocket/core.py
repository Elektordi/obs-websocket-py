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

class Core:

    def __init__(self):
        self.id = 1
        self.thread_recv = None
        self.eventmanager = EventManager()
        self.answers = {}

    def connect(self, host, port):
        try:
            self.ws = websocket.WebSocket()
            LOG.info("Connecting...")
            self.ws.connect("ws://%s:%d"%(host, port))
            LOG.info("Connected!")
        except socket.error, e:
            raise exceptions.ConnectionFailure(str(e))
    
    def reconnect(self):
        # TODO
        raise exceptions.ConnectionFailure("Reconnect not implemented")
            
    def disconnect(self):
        LOG.info("Disconnecting...")
        if not self.thread_recv is None:
            self.thread_recv.running = False
        try:
            self.ws.close()
        except socket.error, e:
            pass
        
    def auth(self, password):
        auth_payload = {"request-type": "GetAuthRequired", "message-id": str(self.id)}
        self.id += 1
        self.ws.send(json.dumps(auth_payload))
        result = json.loads(self.ws.recv())

        if result['authRequired']:
            secret = base64.b64encode(hashlib.sha256(password + result['salt']).digest())
            auth = base64.b64encode(hashlib.sha256(secret + result['challenge']).digest())

            auth_payload = {"request-type": "Authenticate", "message-id": str(self.id), "auth": auth}
            self.id += 1
            self.ws.send(json.dumps(auth_payload))
            result = json.loads(self.ws.recv())
            if result['status'] != 'ok':
                raise exceptions.ConnectionFailure(result['error'])      
        pass
        
    def run_threads(self):
        if not self.thread_recv is None:
            self.thread_recv.running = False
        self.thread_recv = RecvThread(self)
        self.thread_recv.start()
    
    def call(self, obj):
        if not isinstance(obj, base_classes.BaseRequest):
            raise exceptions.ObjectError("Call parameter is not a request object")
        payload = obj.data()
        r = self.send(payload)
        obj.input(r)
        return obj
        
    def send(self, data):
        id = str(self.id)
        self.id += 1
        data["message-id"] = id
        LOG.debug("Sending message id %s: %r"%(id, data))
        self.ws.send(json.dumps(data))
        return self.waitmessage(id)
        
    def waitmessage(self, id):
        timeout = time.time() + 60 # Timeout = 60s
        while time.time() < timeout:
            if id in self.answers:
                return self.answers.pop(id)
            time.sleep(0.1)    
        raise exceptions.MessageTimeout("No answer for message %s"%(id))
            
        

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
                result = json.loads(message)
                if 'update-type' in result:
                    LOG.debug("Got message: %r"%(result))
                    #self.core.eventmanager.trigger(result)
                    obj = self.buildEvent(result)
                    self.core.eventmanager.trigger(obj)
                elif 'message-id' in result:
                    LOG.debug("Got answer for id %s: %r"%(result['message-id'], result))
                    self.core.answers[result['message-id']] = result
                else:
                    LOG.warning("Unknow message: %r"%(result))
            except websocket.WebSocketConnectionClosedException:
                if self.running:
                    self.core.reconnect()
            except (ValueError, exceptions.ObjectError), e:
                LOG.warning("Invalid message: %s (%s)"%(message, e))
        # end while
        LOG.debug("RecvThread ended.")
            
    def buildEvent(self, data):
        name = data["update-type"]
        try:
            obj = getattr(events, name)()
        except AttributeError:
            raise exceptions.ObjectError("Invalid event %s"%(name))
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
    
