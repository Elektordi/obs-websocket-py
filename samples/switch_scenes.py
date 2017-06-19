#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests


host = "localhost"
port = 4444
password = "secret"

ws = obsws(host, port, password)
ws.connect()

try:
    scenes = ws.call(requests.GetSceneList())
    for s in scenes.getScenes():
        name = s['name']
        print "Switching to %s"%(name)
        ws.call(requests.SetCurrentScene(name))
        time.sleep(2)

    print "End of list"
    
except KeyboardInterrupt:
    pass
    
ws.disconnect()
