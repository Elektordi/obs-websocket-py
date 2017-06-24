#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import core

class obsws:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password

        self._core = core.Core()

    def connect(self):
        self._core.connect(self.host, self.port)
        self._core.auth(self.password)
        self._core.run_threads()

    def disconnect(self):
        self._core.disconnect()

    def register(self, function, event = None):
        self._core.eventmanager.register(function, event)

    def unregister(self, function, event = None):
        self._core.eventmanager.unregister(function, event)

    def call(self, obj):
        return self._core.call(obj)

    def send(self, data):
        return self._core.send(data)

