#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, events

host = "localhost"
port = 4444
password = "secret"

def on_event(message):
    print "Got message: %r"%(message)
    
def on_switch(message):
    print "You changed the scene to %s"%(message.getSceneName())

ws = obsws(host, port, password)
ws.register(on_event)
ws.register(on_switch, events.SwitchScenes)
ws.connect()

try:
    print "OK"
    time.sleep(10)
    print "END"

except KeyboardInterrupt:
    pass

ws.disconnect()
