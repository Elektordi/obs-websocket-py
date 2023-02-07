#!/usr/bin/env python3

import sys
import time

import logging
logging.basicConfig(level=logging.DEBUG)

sys.path.append('../')
from obswebsocket import obsws  # noqa: E402

host = "localhost"
port = 4455
password = "secret"


def on_connect(obs):
    print("on_connect({})".format(obs))


def on_disconnect(obs):
    print("on_disconnect({})".format(obs))


ws = obsws(host, port, password, authreconnect=1, on_connect=on_connect, on_disconnect=on_disconnect)
ws.connect()

try:
    print("Running. Now try to start/quit obs multiple times!")
    time.sleep(30)
    print("End of test.")

except KeyboardInterrupt:
    pass

ws.disconnect()
