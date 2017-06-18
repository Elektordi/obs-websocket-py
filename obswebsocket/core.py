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

from . import exceptions

class Core:

    def __init__(self):
        self.id = 1
        self.thread_recv = None
        self.eventmanager = EventManager()
        self.answers = {}

    def connect(self, host, port):
        try:
            self.ws = websocket.WebSocket()
            self.ws.connect("ws://%s:%d"%(host, port))
        except socket.error, e:
            raise exceptions.ConnectionFailure(str(e))
    
    def reconnect(self):
        # TODO
        raise exceptions.ConnectionFailure("Reconnect not implemented")
            
    def disconnect(self):
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
        
    def send(self, data):
        id = str(self.id)
        self.id += 1
        data["message-id"] = id
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
                    self.core.eventmanager.trigger(result)
                elif 'message-id' in result:
                    self.core.answers[result['message-id']] = result
                else:
                    print "Unknow message: %r"%(result)
            except websocket.WebSocketConnectionClosedException:
                if self.running:
                    self.core.reconnect()
            except ValueError:
                print "Invalid message: %s"%(message)
            
            
class EventManager:

    def __init__(self):
        self.functions = []
    
    def register(self, hook):
        self.functions.append(hook)
        
    def unregister(self, hook):
        self.functions.remove(hook)
        
    def trigger(self, data):
        for f in self.functions:
            f(data)
    
