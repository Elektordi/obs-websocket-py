#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

sys.path.append('../')
from obswebsocket import obsws

host = "localhost"
port = 4444
password = "secret"

def on_event(message):
    print "Got message: %r"%(message)

ws = obsws(host, port, password)
ws.register(on_event)
ws.connect()

print "OK"
time.sleep(10)
print "END"

ws.disconnect()
