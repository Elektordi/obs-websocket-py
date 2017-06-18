#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

sys.path.append('../')
from obswebsocket import obsws

host = "localhost"
port = 4444
password = "secret"

ws = obsws(host, port, password)
ws.connect()

scenes = ws.send({"request-type": "GetSceneList"})
for s in scenes['scenes']:
    name = s['name']
    print "Switching to %s"%(name)
    ws.send({"request-type": "SetCurrentScene", "scene-name": name})
    time.sleep(2)

print "End of list"
ws.disconnect()
