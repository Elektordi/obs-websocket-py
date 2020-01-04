# obs-websocket-py
Python library to communicate with an [obs-websocket](https://github.com/Palakis/obs-websocket) server.

_Licensed under the MIT License_

## Project pages

GitHub project: https://github.com/Elektordi/obs-websocket-py

PyPI package: https://pypi.org/project/obs-websocket-py/

## Installation

Just run `pip install obs-websocket-py` in your Python venv or directly on your system.

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
 |  Simple usage:
 |      >>> import obswebsocket, obswebsocket.requests
 |      >>> client = obswebsocket.obsws("localhost", 4444, "secret")
 |      >>> client.connect()
 |      >>> client.call(obswebsocket.requests.GetVersion()).getObsWebsocketVersion()
 |      u'4.1.0'
 |      >>> client.disconnect()
 |      
 |  For advanced usage, including events callback, see the 'samples' directory.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, host=None, port=4444, password='')
 |      Construct a new obsws wrapper
 |      
 |      :param host: Hostname to connect to
 |      :param port: TCP Port to connect to (Default is 4444)
 |      :param password: Password for the websocket server (Leave this field empty if no auth enabled
 |          on the server)
 |  
 |  call(self, obj)
 |      Make a call to the OBS server through the Websocket.
 |      
 |      :param obj: Request (class from obswebsocket.requests module) to send to the server.
 |      :return: Request object populated with response data.
 |  
 |  connect(self, host=None, port=None)
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
 |  register(self, function, event=None)
 |      Register a new hook in the websocket client
 |      
 |      :param function: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) to trigger the hook on.
 |          Default is None, which means trigger on all events.
 |      :return: Nothing
 |  
 |  send(self, data)
 |      Make a raw json call to the OBS server through the Websocket.
 |      
 |      :param obj: Request (python dict) to send to the server. Do not include field "message-id".
 |      :return: Response (python dict) from the server.
 |  
 |  unregister(self, function, event=None)
 |      Unregister a new hook in the websocket client
 |      
 |      :param function: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) which triggered the hook on.
 |          Default is None, which means unregister this function for all events.
 |      :return: Nothing
```

## Problems?

Please check on [Github project issues](https://github.com/Elektordi/obs-websocket-py/issues), and if nobody else have experienced it before, you can [file a new issue](https://github.com/Elektordi/obs-websocket-py/issues/new).

