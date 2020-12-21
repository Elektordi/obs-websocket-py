# obs-websocket-py
Python library & CLI to communicate with an [obs-websocket](https://github.com/Palakis/obs-websocket) server.

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

There is also a simple CLI provided with the installation. It can be used in variety of ways, but is not meant to cover all use cases.

```
$ obs-web-cli --help
OBS Studio CLI using OBS Websocket Plugin

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Hostname to connect to (default: localhost)
  --port PORT           Port to connect to (default: 4444)
  --password PASSWORD   Password to use. Defaults to OBS_WEBSOCKET_PASS env
                        var (default: None)
  --debug               Enable debugging output (default: False)

Recognized commands:
  {GetStreamingStatus,StartStopStreaming,StartStreaming,StopStreaming,SetStreamSettings,GetStreamSettings,SaveStreamSettings,SendCaptions,GetStudioModeStatus,GetPreviewScene,SetPreviewScene,TransitionToProgram,EnableStudioMode,DisableStudioMode,ToggleStudioMode,ListOutputs,GetOutputInfo,StartOutput,StopOutput,StartStopReplayBuffer,StartReplayBuffer,StopReplayBuffer,SaveReplayBuffer,SetCurrentScene,GetCurrentScene,GetSceneList,ReorderSceneItems,SetCurrentProfile,GetCurrentProfile,ListProfiles,GetVersion,GetAuthRequired,Authenticate,SetHeartbeat,SetFilenameFormatting,GetFilenameFormatting,GetStats,BroadcastCustomMessage,GetVideoInfo,StartStopRecording,StartRecording,StopRecording,PauseRecording,ResumeRecording,SetRecordingFolder,GetRecordingFolder,GetSourcesList,GetSourceTypesList,GetVolume,SetVolume,GetMute,SetMute,ToggleMute,SetSyncOffset,GetSyncOffset,GetSourceSettings,SetSourceSettings,GetTextGDIPlusProperties,SetTextGDIPlusProperties,GetTextFreetype2Properties,SetTextFreetype2Properties,GetBrowserSourceProperties,SetBrowserSourceProperties,GetSpecialSources,GetSourceFilters,GetSourceFilterInfo,AddFilterToSource,RemoveFilterFromSource,ReorderSourceFilter,MoveSourceFilter,SetSourceFilterSettings,SetSourceFilterVisibility,TakeSourceScreenshot,SetCurrentSceneCollection,GetCurrentSceneCollection,ListSceneCollections,GetTransitionList,GetCurrentTransition,SetCurrentTransition,SetTransitionDuration,GetTransitionDuration,GetSceneItemProperties,SetSceneItemProperties,ResetSceneItem,SetSceneItemRender,SetSceneItemPosition,SetSceneItemTransform,SetSceneItemCrop,DeleteSceneItem,DuplicateSceneItem}
```

Simple arguments can be provided directly on the command line:

```
$ obs-web-cli SetCurrentSceneCollection "Untitled"
INFO:obswebsocket.core:Connecting...
INFO:obswebsocket.core:Connected!
{}
INFO:obswebsocket.core:Disconnecting...
```

More complex arguments might require passing in a JSON string `json:` prefix. For example:

```
$ obs-web-cli SetSourceSettings "gif_source1" 'json:{"looping": true}' ffmpeg_source
INFO:obswebsocket.core:Connecting...
INFO:obswebsocket.core:Connected!
{
    "sourceName": "gif_source1",
    "sourceSettings": {
        "hw_decode": true,
        "local_file": "/images/demo.gif",
        "looping": true
    },
    "sourceType": "ffmpeg_source"
}
INFO:obswebsocket.core:Disconnecting...
```

## Problems?

Please check on [Github project issues](https://github.com/Elektordi/obs-websocket-py/issues), and if nobody else have experienced it before, you can [file a new issue](https://github.com/Elektordi/obs-websocket-py/issues/new).

