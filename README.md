# obs-websocket-py
Python3 library to communicate with an [obs-websocket](https://github.com/Palakis/obs-websocket) server.

_Licensed under the MIT License_

## Project pages

GitHub project: https://github.com/Elektordi/obs-websocket-py

PyPI package: https://pypi.org/project/obs-websocket-py/

## Installation

Just run `pip3 install obs-websocket-py` in your Python venv or directly on your system.

For manual install, git clone the github repo and copy the directory **obswebsocket** in your python project root.

**Requires**: websocket-client (from pip)

## Usage

See python scripts in the [samples](https://github.com/Elektordi/obs-websocket-py/tree/master/samples) directory.

Or take a look at the documentation below:

_Output of `pydoc obswebsocket.core.obsws`:_

```
Help on class obsws in obswebsocket.core:

obswebsocket.core.obsws = class obsws
 |  Core class for using obs-websocket-py
 |  
 |  Simple usage: (v5 api)
 |      >>> from obswebsocket import obsws, requests
 |      >>> client = obsws("localhost", 4455, "secret")
 |      >>> client.connect()
 |      >>> client.call(requests.GetVersion()).getObsVersion()
 |      '29.0.0'
 |      >>> client.disconnect()
 |  
 |  Legacy usage: (v4 api)
 |      >>> from obswebsocket import obsws, requests
 |      >>> client = obsws("localhost", 4444, "secret", legacy=True)
 |      >>> client.connect()
 |      >>> client.call(requests.GetVersion()).getObsStudioVersion()
 |      '25.0.0'
 |      >>> client.disconnect()
 |  
 |  For advanced usage, including events callback, see the 'samples' directory.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, host='localhost', port=4444, password='', legacy=None, timeout=60, authreconnect=0, on_connect=None, on_disconnect=None)
 |      Construct a new obsws wrapper
 |      
 |      :param host: Hostname to connect to
 |      :param port: TCP Port to connect to (Default is 4444)
 |      :param password: Password for the websocket server (Leave this field empty if auth is not enabled)
 |      :param legacy: Server is using old obs-websocket protocol (v4). Default is v5 (False) except if port is 4444.
 |      :param timeout: How much seconds to wait for an answer after sending a request.
 |      :param authreconnect: Try to reconnect if websocket is closed, value is number of seconds between attemps.
 |      :param on_connect: Function to call after successful connect, with parameter (obsws)
 |      :param on_disconnect: Function to call after successful disconnect, with parameter (obsws)
 |  
 |  call(self, obj)
 |      Make a call to the OBS server through the Websocket.
 |      
 |      :param obj: Request (class from obswebsocket.requests module) to send
 |          to the server.
 |      :return: Request object populated with response data.
 |  
 |  connect(self)
 |      Connect to the websocket server
 |      
 |      :return: Nothing
 |  
 |  disconnect(self)
 |      Disconnect from websocket server
 |      
 |      :return: Nothing
 |  
 |  reconnect(self)
 |      Restart the connection to the websocket server
 |      
 |      :return: Nothing
 |  
 |  register(self, func, event=None)
 |      Register a new hook in the websocket client
 |      
 |      :param func: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) to trigger
 |          the hook on. Default is None, which means trigger on all events.
 |      :return: Nothing
 |  
 |  unregister(self, func, event=None)
 |      Unregister a new hook in the websocket client
 |      
 |      :param func: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) which
 |          triggered the hook on. Default is None, which means unregister this
 |          function for all events.
 |      :return: Nothing
```

## Problems?

Please check on [Github project issues](https://github.com/Elektordi/obs-websocket-py/issues), and if nobody else have experienced it before, you can [file a new issue](https://github.com/Elektordi/obs-websocket-py/issues/new).

