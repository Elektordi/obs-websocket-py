#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (Generated on 2020-11-18 11:01:42.362936) #

from .base_classes import Baserequests


class GetVersion(Baserequests):
    """Returns the latest version of the plugin and the API.

    :Returns:
       *version*
            type: double
            OBSRemote compatible API version. Fixed to 1.1 for retrocompatibility.
       *obs_websocket_version*
            type: String
            obs-websocket plugin version.
       *obs_studio_version*
            type: String
            OBS Studio program version.
       *available_requests*
            type: String
            List of available request types, formatted as a comma-separated list string (e.g. : "Method1,Method2,Method3").
       *supported_image_export_formats*
            type: String
            List of supported formats for features that use image export (like the TakeSourceScreenshot request type) formatted as a comma-separated list string
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetVersion'
        self.datain['version'] = None
        self.datain['obs-studio-version'] = None
        self.datain['obs-websocket-version'] = None
        self.datain['supported-image-export-formats'] = None
        self.datain['available-requests'] = None

    def getVersion(self):
        return self.datain['version']

    def getObsStudioVersion(self):
        return self.datain['obs-studio-version']

    def getObsWebsocketVersion(self):
        return self.datain['obs-websocket-version']

    def getSupportedImageExportFormats(self):
        return self.datain['supported-image-export-formats']

    def getAvailableRequests(self):
        return self.datain['available-requests']


class GetAuthRequired(Baserequests):
    """Tells the client if authentication is required. If so, returns authentication parameters `challenge`
and `salt` (see "Authentication" for more information).

    :Returns:
       *authRequired*
            type: boolean
            Indicates whether authentication is required.
       *challenge*
            type: String (optional)
            
       *salt*
            type: String (optional)
            
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetAuthRequired'
        self.datain['salt'] = None
        self.datain['authRequired'] = None
        self.datain['challenge'] = None

    def getSalt(self):
        return self.datain['salt']

    def getAuthrequired(self):
        return self.datain['authRequired']

    def getChallenge(self):
        return self.datain['challenge']


class Authenticate(Baserequests):
    """Attempt to authenticate the client to the server.

    :Arguments:
       *auth*
            type: String
            Response to the auth challenge (see "Authentication" for more information).
    """

    def __init__(self, auth):
        Baserequests.__init__(self)
        self.name = 'Authenticate'
        self.dataout['auth'] = auth


class SetHeartbeat(Baserequests):
    """Enable/disable sending of the Heartbeat event

    :Arguments:
       *enable*
            type: boolean
            Starts/Stops emitting heartbeat messages
    """

    def __init__(self, enable):
        Baserequests.__init__(self)
        self.name = 'SetHeartbeat'
        self.dataout['enable'] = enable


class SetFilenameFormatting(Baserequests):
    """Set the filename formatting string

    :Arguments:
       *filename_formatting*
            type: String
            Filename formatting string to set.
    """

    def __init__(self, filename_formatting):
        Baserequests.__init__(self)
        self.name = 'SetFilenameFormatting'
        self.dataout['filename-formatting'] = filename_formatting


class GetFilenameFormatting(Baserequests):
    """Get the filename formatting string

    :Returns:
       *filename_formatting*
            type: String
            Current filename formatting string.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetFilenameFormatting'
        self.datain['filename-formatting'] = None

    def getFilenameFormatting(self):
        return self.datain['filename-formatting']


class GetStats(Baserequests):
    """Get OBS stats (almost the same info as provided in OBS' stats window)

    :Returns:
       *stats*
            type: OBSStats
            [OBS stats](#obsstats)
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetStats'
        self.datain['stats'] = None

    def getStats(self):
        return self.datain['stats']


class BroadcastCustomMessage(Baserequests):
    """Broadcast custom message to all connected WebSocket clients

    :Arguments:
       *realm*
            type: String
            Identifier to be choosen by the client
       *data*
            type: Object
            User-defined data
    """

    def __init__(self, data, realm):
        Baserequests.__init__(self)
        self.name = 'BroadcastCustomMessage'
        self.dataout['data'] = data
        self.dataout['realm'] = realm


class GetVideoInfo(Baserequests):
    """Get basic OBS video information

    :Returns:
       *baseWidth*
            type: int
            Base (canvas) width
       *baseHeight*
            type: int
            Base (canvas) height
       *outputWidth*
            type: int
            Output width
       *outputHeight*
            type: int
            Output height
       *scaleType*
            type: String
            Scaling method used if output size differs from base size
       *fps*
            type: double
            Frames rendered per second
       *videoFormat*
            type: String
            Video color format
       *colorSpace*
            type: String
            Color space for YUV
       *colorRange*
            type: String
            Color range (full or partial)
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetVideoInfo'
        self.datain['baseHeight'] = None
        self.datain['colorRange'] = None
        self.datain['baseWidth'] = None
        self.datain['fps'] = None
        self.datain['videoFormat'] = None
        self.datain['scaleType'] = None
        self.datain['colorSpace'] = None
        self.datain['outputWidth'] = None
        self.datain['outputHeight'] = None

    def getBaseheight(self):
        return self.datain['baseHeight']

    def getColorrange(self):
        return self.datain['colorRange']

    def getBasewidth(self):
        return self.datain['baseWidth']

    def getFps(self):
        return self.datain['fps']

    def getVideoformat(self):
        return self.datain['videoFormat']

    def getScaletype(self):
        return self.datain['scaleType']

    def getColorspace(self):
        return self.datain['colorSpace']

    def getOutputwidth(self):
        return self.datain['outputWidth']

    def getOutputheight(self):
        return self.datain['outputHeight']


class OpenProjector(Baserequests):
    """Open a projector window or create a projector on a monitor. Requires OBS v24.0.4 or newer.

    :Arguments:
       *type*
            type: String (Optional)
            Type of projector: `Preview` (default), `Source`, `Scene`, `StudioProgram`, or `Multiview` (case insensitive).
       *monitor*
            type: int (Optional)
            Monitor to open the projector on. If -1 or omitted, opens a window.
       *geometry*
            type: String (Optional)
            Size and position of the projector window (only if monitor is -1). Encoded in Base64 using [Qt's geometry encoding](https://doc.qt.io/qt-5/qwidget.html#saveGeometry). Corresponds to OBS's saved projectors.
       *name*
            type: String (Optional)
            Name of the source or scene to be displayed (ignored for other projector types).
    """

    def __init__(self, name, type, monitor, geometry):
        Baserequests.__init__(self)
        self.name = 'OpenProjector'
        self.dataout['name'] = name
        self.dataout['type'] = type
        self.dataout['monitor'] = monitor
        self.dataout['geometry'] = geometry


class TriggerHotkeyByName(Baserequests):
    """Executes hotkey routine, identified by hotkey unique name

    :Arguments:
       *hotkeyName*
            type: String
            Unique name of the hotkey, as defined when registering the hotkey (e.g. "ReplayBuffer.Save")
    """

    def __init__(self, hotkeyName):
        Baserequests.__init__(self)
        self.name = 'TriggerHotkeyByName'
        self.dataout['hotkeyName'] = hotkeyName


class TriggerHotkeyBySequence(Baserequests):
    """Executes hotkey routine, identified by bound combination of keys. A single key combination might trigger multiple hotkey routines depending on user settings

    :Arguments:
       *keyId*
            type: String
            Main key identifier (e.g. `OBS_KEY_A` for key "A"). Available identifiers [here](https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h)
       *keyModifiers*
            type: Object (Optional)
            Optional key modifiers object. False entries can be ommitted
       *keyModifiers.shift*
            type: boolean
            Trigger Shift Key
       *keyModifiers.alt*
            type: boolean
            Trigger Alt Key
       *keyModifiers.control*
            type: boolean
            Trigger Control (Ctrl) Key
       *keyModifiers.command*
            type: boolean
            Trigger Command Key (Mac)
    """

    def __init__(self, keyId, keyModifiers):
        Baserequests.__init__(self)
        self.name = 'TriggerHotkeyBySequence'
        self.dataout['keyId'] = keyId
        self.dataout['keyModifiers'] = keyModifiers


class PlayPauseMedia(Baserequests):
    """Pause or play a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *playPause*
            type: boolean
            Whether to pause or play the source. `false` for play, `true` for pause.
    """

    def __init__(self, playPause, sourceName):
        Baserequests.__init__(self)
        self.name = 'PlayPauseMedia'
        self.dataout['playPause'] = playPause
        self.dataout['sourceName'] = sourceName


class RestartMedia(Baserequests):
    """Restart a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'RestartMedia'
        self.dataout['sourceName'] = sourceName


class StopMedia(Baserequests):
    """Stop a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'StopMedia'
        self.dataout['sourceName'] = sourceName


class NextMedia(Baserequests):
    """Skip to the next media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'NextMedia'
        self.dataout['sourceName'] = sourceName


class PreviousMedia(Baserequests):
    """Go to the previous media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'PreviousMedia'
        self.dataout['sourceName'] = sourceName


class GetMediaDuration(Baserequests):
    """Get the length of media in milliseconds. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
Note: For some reason, for the first 5 or so seconds that the media is playing, the total duration can be off by upwards of 50ms.

    :Arguments:
       *sourceName*
            type: String
            Source name.
    :Returns:
       *mediaDuration*
            type: int
            The total length of media in milliseconds..
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetMediaDuration'
        self.datain['mediaDuration'] = None
        self.dataout['sourceName'] = sourceName

    def getMediaduration(self):
        return self.datain['mediaDuration']


class GetMediaTime(Baserequests):
    """Get the current timestamp of media in milliseconds. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    :Returns:
       *timestamp*
            type: int
            The time in milliseconds since the start of the media.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetMediaTime'
        self.datain['timestamp'] = None
        self.dataout['sourceName'] = sourceName

    def getTimestamp(self):
        return self.datain['timestamp']


class SetMediaTime(Baserequests):
    """Set the timestamp of a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *timestamp*
            type: int
            Milliseconds to set the timestamp to.
    """

    def __init__(self, timestamp, sourceName):
        Baserequests.__init__(self)
        self.name = 'SetMediaTime'
        self.dataout['timestamp'] = timestamp
        self.dataout['sourceName'] = sourceName


class ScrubMedia(Baserequests):
    """Scrub media using a supplied offset. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
Note: Due to processing/network delays, this request is not perfect. The processing rate of this request has also not been tested.

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *timeOffset*
            type: int
            Millisecond offset (positive or negative) to offset the current media position.
    """

    def __init__(self, timeOffset, sourceName):
        Baserequests.__init__(self)
        self.name = 'ScrubMedia'
        self.dataout['timeOffset'] = timeOffset
        self.dataout['sourceName'] = sourceName


class GetMediaState(Baserequests):
    """Get the current playing state of a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    :Returns:
       *mediaState*
            type: String
            The media state of the provided source. States: `none`, `playing`, `opening`, `buffering`, `paused`, `stopped`, `ended`, `error`, `unknown`
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetMediaState'
        self.datain['mediaState'] = None
        self.dataout['sourceName'] = sourceName

    def getMediastate(self):
        return self.datain['mediaState']


class GetMediaSourcesList(Baserequests):
    """List the media state of all media sources (vlc and media source)

    :Returns:
       *mediaSources*
            type: Array<Object>
            Array of sources
       *mediaSources.*.sourceName*
            type: String
            Unique source name
       *mediaSources.*.sourceKind*
            type: String
            Unique source internal type (a.k.a `ffmpeg_source` or `vlc_source`)
       *mediaSources.*.mediaState*
            type: String
            The current state of media for that source. States: `none`, `playing`, `opening`, `buffering`, `paused`, `stopped`, `ended`, `error`, `unknown`
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetMediaSourcesList'
        self.datain['mediaSources'] = None

    def getMediasources(self):
        return self.datain['mediaSources']


class GetSourcesList(Baserequests):
    """List all sources available in the running OBS instance

    :Returns:
       *sources*
            type: Array<Object>
            Array of sources
       *sources.*.name*
            type: String
            Unique source name
       *sources.*.typeId*
            type: String
            Non-unique source internal type (a.k.a kind)
       *sources.*.type*
            type: String
            Source type. Value is one of the following: "input", "filter", "transition", "scene" or "unknown"
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetSourcesList'
        self.datain['sources'] = None

    def getSources(self):
        return self.datain['sources']


class GetSourceTypesList(Baserequests):
    """Get a list of all available sources types

    :Returns:
       *types*
            type: Array<Object>
            Array of source types
       *types.*.typeId*
            type: String
            Non-unique internal source type ID
       *types.*.displayName*
            type: String
            Display name of the source type
       *types.*.type*
            type: String
            Type. Value is one of the following: "input", "filter", "transition" or "other"
       *types.*.defaultSettings*
            type: Object
            Default settings of this source type
       *types.*.caps*
            type: Object
            Source type capabilities
       *types.*.caps.isAsync*
            type: Boolean
            True if source of this type provide frames asynchronously
       *types.*.caps.hasVideo*
            type: Boolean
            True if sources of this type provide video
       *types.*.caps.hasAudio*
            type: Boolean
            True if sources of this type provide audio
       *types.*.caps.canInteract*
            type: Boolean
            True if interaction with this sources of this type is possible
       *types.*.caps.isComposite*
            type: Boolean
            True if sources of this type composite one or more sub-sources
       *types.*.caps.doNotDuplicate*
            type: Boolean
            True if sources of this type should not be fully duplicated
       *types.*.caps.doNotSelfMonitor*
            type: Boolean
            True if sources of this type may cause a feedback loop if it's audio is monitored and shouldn't be
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetSourceTypesList'
        self.datain['types'] = None

    def getTypes(self):
        return self.datain['types']


class GetVolume(Baserequests):
    """Get the volume of the specified source. Default response uses mul format, NOT SLIDER PERCENTAGE.

    :Arguments:
       *source*
            type: String
            Source name.
       *useDecibel*
            type: boolean (optional)
            Output volume in decibels of attenuation instead of amplitude/mul.
    :Returns:
       *name*
            type: String
            Source name.
       *volume*
            type: double
            Volume of the source. Between `0.0` and `1.0` if using mul, under `0.0` if using dB (since it is attenuating).
       *muted*
            type: boolean
            Indicates whether the source is muted.
    """

    def __init__(self, source, useDecibel=None):
        Baserequests.__init__(self)
        self.name = 'GetVolume'
        self.datain['name'] = None
        self.datain['muted'] = None
        self.datain['volume'] = None
        self.dataout['source'] = source
        self.dataout['useDecibel'] = useDecibel

    def getName(self):
        return self.datain['name']

    def getMuted(self):
        return self.datain['muted']

    def getVolume(self):
        return self.datain['volume']


class SetVolume(Baserequests):
    """Set the volume of the specified source. Default request format uses mul, NOT SLIDER PERCENTAGE.

    :Arguments:
       *source*
            type: String
            Source name.
       *volume*
            type: double
            Desired volume. Must be between `0.0` and `1.0` for mul, and under 0.0 for dB. Note: OBS will interpret dB values under -100.0 as Inf.
       *useDecibel*
            type: boolean (optional)
            Interperet `volume` data as decibels instead of amplitude/mul.
    """

    def __init__(self, volume, source, useDecibel=None):
        Baserequests.__init__(self)
        self.name = 'SetVolume'
        self.dataout['volume'] = volume
        self.dataout['source'] = source
        self.dataout['useDecibel'] = useDecibel


class GetMute(Baserequests):
    """Get the mute status of a specified source.

    :Arguments:
       *source*
            type: String
            Source name.
    :Returns:
       *name*
            type: String
            Source name.
       *muted*
            type: boolean
            Mute status of the source.
    """

    def __init__(self, source):
        Baserequests.__init__(self)
        self.name = 'GetMute'
        self.datain['name'] = None
        self.datain['muted'] = None
        self.dataout['source'] = source

    def getName(self):
        return self.datain['name']

    def getMuted(self):
        return self.datain['muted']


class SetMute(Baserequests):
    """Sets the mute status of a specified source.

    :Arguments:
       *source*
            type: String
            Source name.
       *mute*
            type: boolean
            Desired mute status.
    """

    def __init__(self, mute, source):
        Baserequests.__init__(self)
        self.name = 'SetMute'
        self.dataout['mute'] = mute
        self.dataout['source'] = source


class ToggleMute(Baserequests):
    """Inverts the mute status of a specified source.

    :Arguments:
       *source*
            type: String
            Source name.
    """

    def __init__(self, source):
        Baserequests.__init__(self)
        self.name = 'ToggleMute'
        self.dataout['source'] = source


class GetAudioActive(Baserequests):
    """Get the audio's active status of a specified source.

    :Arguments:
       *sourceName*
            type: String
            Source name.
    :Returns:
       *audioActive*
            type: boolean
            Audio active status of the source.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetAudioActive'
        self.datain['audioActive'] = None
        self.dataout['sourceName'] = sourceName

    def getAudioactive(self):
        return self.datain['audioActive']


class SetSourceName(Baserequests):
    """

Note: If the new name already exists as a source, obs-websocket will return an error.

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *newName*
            type: String
            New source name.
    """

    def __init__(self, newName, sourceName):
        Baserequests.__init__(self)
        self.name = 'SetSourceName'
        self.dataout['newName'] = newName
        self.dataout['sourceName'] = sourceName


class SetSyncOffset(Baserequests):
    """Set the audio sync offset of a specified source.

    :Arguments:
       *source*
            type: String
            Source name.
       *offset*
            type: int
            The desired audio sync offset (in nanoseconds).
    """

    def __init__(self, offset, source):
        Baserequests.__init__(self)
        self.name = 'SetSyncOffset'
        self.dataout['offset'] = offset
        self.dataout['source'] = source


class GetSyncOffset(Baserequests):
    """Get the audio sync offset of a specified source.

    :Arguments:
       *source*
            type: String
            Source name.
    :Returns:
       *name*
            type: String
            Source name.
       *offset*
            type: int
            The audio sync offset (in nanoseconds).
    """

    def __init__(self, source):
        Baserequests.__init__(self)
        self.name = 'GetSyncOffset'
        self.datain['name'] = None
        self.datain['offset'] = None
        self.dataout['source'] = source

    def getName(self):
        return self.datain['name']

    def getOffset(self):
        return self.datain['offset']


class GetSourceSettings(Baserequests):
    """Get settings of the specified source

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *sourceType*
            type: String (optional)
            Type of the specified source. Useful for type-checking if you expect a specific settings schema.
    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceType*
            type: String
            Type of the specified source
       *sourceSettings*
            type: Object
            Source settings (varies between source types, may require some probing around).
    """

    def __init__(self, sourceName, sourceType=None):
        Baserequests.__init__(self)
        self.name = 'GetSourceSettings'
        self.datain['sourceSettings'] = None
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None
        self.dataout['sourceName'] = sourceName
        self.dataout['sourceType'] = sourceType

    def getSourcesettings(self):
        return self.datain['sourceSettings']

    def getSourcename(self):
        return self.datain['sourceName']

    def getSourcetype(self):
        return self.datain['sourceType']


class SetSourceSettings(Baserequests):
    """Set settings of the specified source.

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *sourceType*
            type: String (optional)
            Type of the specified source. Useful for type-checking to avoid settings a set of settings incompatible with the actual source's type.
       *sourceSettings*
            type: Object
            Source settings (varies between source types, may require some probing around).
    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceType*
            type: String
            Type of the specified source
       *sourceSettings*
            type: Object
            Updated source settings
    """

    def __init__(self, sourceSettings, sourceName, sourceType=None):
        Baserequests.__init__(self)
        self.name = 'SetSourceSettings'
        self.datain['sourceSettings'] = None
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None
        self.dataout['sourceSettings'] = sourceSettings
        self.dataout['sourceName'] = sourceName
        self.dataout['sourceType'] = sourceType

    def getSourcesettings(self):
        return self.datain['sourceSettings']

    def getSourcename(self):
        return self.datain['sourceName']

    def getSourcetype(self):
        return self.datain['sourceType']


class GetTextGDIPlusProperties(Baserequests):
    """Get the current properties of a Text GDI Plus source.

    :Arguments:
       *source*
            type: String
            Source name.
    :Returns:
       *source*
            type: String
            Source name.
       *align*
            type: String
            Text Alignment ("left", "center", "right").
       *bk_color*
            type: int
            Background color.
       *bk_opacity*
            type: int
            Background opacity (0-100).
       *chatlog*
            type: boolean
            Chat log.
       *chatlog_lines*
            type: int
            Chat log lines.
       *color*
            type: int
            Text color.
       *extents*
            type: boolean
            Extents wrap.
       *extents_cx*
            type: int
            Extents cx.
       *extents_cy*
            type: int
            Extents cy.
       *file*
            type: String
            File path name.
       *read_from_file*
            type: boolean
            Read text from the specified file.
       *font*
            type: Object
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
       *font.face*
            type: String
            Font face.
       *font.flags*
            type: int
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int
            Font text size.
       *font.style*
            type: String
            Font Style (unknown function).
       *gradient*
            type: boolean
            Gradient enabled.
       *gradient_color*
            type: int
            Gradient color.
       *gradient_dir*
            type: float
            Gradient direction.
       *gradient_opacity*
            type: int
            Gradient opacity (0-100).
       *outline*
            type: boolean
            Outline.
       *outline_color*
            type: int
            Outline color.
       *outline_size*
            type: int
            Outline size.
       *outline_opacity*
            type: int
            Outline opacity (0-100).
       *text*
            type: String
            Text content to be displayed.
       *valign*
            type: String
            Text vertical alignment ("top", "center", "bottom").
       *vertical*
            type: boolean
            Vertical text enabled.
    """

    def __init__(self, source):
        Baserequests.__init__(self)
        self.name = 'GetTextGDIPlusProperties'
        self.datain['bk_opacity'] = None
        self.datain['read_from_file'] = None
        self.datain['align'] = None
        self.datain['gradient_color'] = None
        self.datain['outline_size'] = None
        self.datain['extents_cy'] = None
        self.datain['file'] = None
        self.datain['outline'] = None
        self.datain['gradient'] = None
        self.datain['outline_color'] = None
        self.datain['color'] = None
        self.datain['extents_cx'] = None
        self.datain['gradient_dir'] = None
        self.datain['gradient_opacity'] = None
        self.datain['extents'] = None
        self.datain['bk_color'] = None
        self.datain['vertical'] = None
        self.datain['font'] = None
        self.datain['text'] = None
        self.datain['outline_opacity'] = None
        self.datain['source'] = None
        self.datain['chatlog'] = None
        self.datain['valign'] = None
        self.datain['chatlog_lines'] = None
        self.dataout['source'] = source

    def getBk_opacity(self):
        return self.datain['bk_opacity']

    def getRead_from_file(self):
        return self.datain['read_from_file']

    def getAlign(self):
        return self.datain['align']

    def getGradient_color(self):
        return self.datain['gradient_color']

    def getOutline_size(self):
        return self.datain['outline_size']

    def getExtents_cy(self):
        return self.datain['extents_cy']

    def getFile(self):
        return self.datain['file']

    def getOutline(self):
        return self.datain['outline']

    def getGradient(self):
        return self.datain['gradient']

    def getOutline_color(self):
        return self.datain['outline_color']

    def getColor(self):
        return self.datain['color']

    def getExtents_cx(self):
        return self.datain['extents_cx']

    def getGradient_dir(self):
        return self.datain['gradient_dir']

    def getGradient_opacity(self):
        return self.datain['gradient_opacity']

    def getExtents(self):
        return self.datain['extents']

    def getBk_color(self):
        return self.datain['bk_color']

    def getVertical(self):
        return self.datain['vertical']

    def getFont(self):
        return self.datain['font']

    def getText(self):
        return self.datain['text']

    def getOutline_opacity(self):
        return self.datain['outline_opacity']

    def getSource(self):
        return self.datain['source']

    def getChatlog(self):
        return self.datain['chatlog']

    def getValign(self):
        return self.datain['valign']

    def getChatlog_lines(self):
        return self.datain['chatlog_lines']


class SetTextGDIPlusProperties(Baserequests):
    """Set the current properties of a Text GDI Plus source.

    :Arguments:
       *source*
            type: String
            Name of the source.
       *align*
            type: String (optional)
            Text Alignment ("left", "center", "right").
       *bk_color*
            type: int (optional)
            Background color.
       *bk_opacity*
            type: int (optional)
            Background opacity (0-100).
       *chatlog*
            type: boolean (optional)
            Chat log.
       *chatlog_lines*
            type: int (optional)
            Chat log lines.
       *color*
            type: int (optional)
            Text color.
       *extents*
            type: boolean (optional)
            Extents wrap.
       *extents_cx*
            type: int (optional)
            Extents cx.
       *extents_cy*
            type: int (optional)
            Extents cy.
       *file*
            type: String (optional)
            File path name.
       *read_from_file*
            type: boolean (optional)
            Read text from the specified file.
       *font*
            type: Object (optional)
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
       *font.face*
            type: String (optional)
            Font face.
       *font.flags*
            type: int (optional)
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int (optional)
            Font text size.
       *font.style*
            type: String (optional)
            Font Style (unknown function).
       *gradient*
            type: boolean (optional)
            Gradient enabled.
       *gradient_color*
            type: int (optional)
            Gradient color.
       *gradient_dir*
            type: float (optional)
            Gradient direction.
       *gradient_opacity*
            type: int (optional)
            Gradient opacity (0-100).
       *outline*
            type: boolean (optional)
            Outline.
       *outline_color*
            type: int (optional)
            Outline color.
       *outline_size*
            type: int (optional)
            Outline size.
       *outline_opacity*
            type: int (optional)
            Outline opacity (0-100).
       *text*
            type: String (optional)
            Text content to be displayed.
       *valign*
            type: String (optional)
            Text vertical alignment ("top", "center", "bottom").
       *vertical*
            type: boolean (optional)
            Vertical text enabled.
       *render*
            type: boolean (optional)
            Visibility of the scene item.
    """

    def __init__(self, source, read_from_file=None, bk_opacity=None, align=None, gradient_color=None, outline_size=None, extents_cy=None, file=None, outline=None, gradient=None, outline_color=None, color=None, extents_cx=None, gradient_dir=None, gradient_opacity=None, extents=None, bk_color=None, vertical=None, font=None, text=None, render=None, outline_opacity=None, valign=None, chatlog=None, chatlog_lines=None):
        Baserequests.__init__(self)
        self.name = 'SetTextGDIPlusProperties'
        self.dataout['source'] = source
        self.dataout['read_from_file'] = read_from_file
        self.dataout['bk_opacity'] = bk_opacity
        self.dataout['align'] = align
        self.dataout['gradient_color'] = gradient_color
        self.dataout['outline_size'] = outline_size
        self.dataout['extents_cy'] = extents_cy
        self.dataout['file'] = file
        self.dataout['outline'] = outline
        self.dataout['gradient'] = gradient
        self.dataout['outline_color'] = outline_color
        self.dataout['color'] = color
        self.dataout['extents_cx'] = extents_cx
        self.dataout['gradient_dir'] = gradient_dir
        self.dataout['gradient_opacity'] = gradient_opacity
        self.dataout['extents'] = extents
        self.dataout['bk_color'] = bk_color
        self.dataout['vertical'] = vertical
        self.dataout['font'] = font
        self.dataout['text'] = text
        self.dataout['render'] = render
        self.dataout['outline_opacity'] = outline_opacity
        self.dataout['valign'] = valign
        self.dataout['chatlog'] = chatlog
        self.dataout['chatlog_lines'] = chatlog_lines


class GetTextFreetype2Properties(Baserequests):
    """Get the current properties of a Text Freetype 2 source.

    :Arguments:
       *source*
            type: String
            Source name.
    :Returns:
       *source*
            type: String
            Source name
       *color1*
            type: int
            Gradient top color.
       *color2*
            type: int
            Gradient bottom color.
       *custom_width*
            type: int
            Custom width (0 to disable).
       *drop_shadow*
            type: boolean
            Drop shadow.
       *font*
            type: Object
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
       *font.face*
            type: String
            Font face.
       *font.flags*
            type: int
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int
            Font text size.
       *font.style*
            type: String
            Font Style (unknown function).
       *from_file*
            type: boolean
            Read text from the specified file.
       *log_mode*
            type: boolean
            Chat log.
       *outline*
            type: boolean
            Outline.
       *text*
            type: String
            Text content to be displayed.
       *text_file*
            type: String
            File path.
       *word_wrap*
            type: boolean
            Word wrap.
    """

    def __init__(self, source):
        Baserequests.__init__(self)
        self.name = 'GetTextFreetype2Properties'
        self.datain['color1'] = None
        self.datain['outline'] = None
        self.datain['text_file'] = None
        self.datain['word_wrap'] = None
        self.datain['color2'] = None
        self.datain['source'] = None
        self.datain['log_mode'] = None
        self.datain['from_file'] = None
        self.datain['custom_width'] = None
        self.datain['font'] = None
        self.datain['text'] = None
        self.datain['drop_shadow'] = None
        self.dataout['source'] = source

    def getColor1(self):
        return self.datain['color1']

    def getOutline(self):
        return self.datain['outline']

    def getText_file(self):
        return self.datain['text_file']

    def getWord_wrap(self):
        return self.datain['word_wrap']

    def getColor2(self):
        return self.datain['color2']

    def getSource(self):
        return self.datain['source']

    def getLog_mode(self):
        return self.datain['log_mode']

    def getFrom_file(self):
        return self.datain['from_file']

    def getCustom_width(self):
        return self.datain['custom_width']

    def getFont(self):
        return self.datain['font']

    def getText(self):
        return self.datain['text']

    def getDrop_shadow(self):
        return self.datain['drop_shadow']


class SetTextFreetype2Properties(Baserequests):
    """Set the current properties of a Text Freetype 2 source.

    :Arguments:
       *source*
            type: String
            Source name.
       *color1*
            type: int (optional)
            Gradient top color.
       *color2*
            type: int (optional)
            Gradient bottom color.
       *custom_width*
            type: int (optional)
            Custom width (0 to disable).
       *drop_shadow*
            type: boolean (optional)
            Drop shadow.
       *font*
            type: Object (optional)
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
       *font.face*
            type: String (optional)
            Font face.
       *font.flags*
            type: int (optional)
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int (optional)
            Font text size.
       *font.style*
            type: String (optional)
            Font Style (unknown function).
       *from_file*
            type: boolean (optional)
            Read text from the specified file.
       *log_mode*
            type: boolean (optional)
            Chat log.
       *outline*
            type: boolean (optional)
            Outline.
       *text*
            type: String (optional)
            Text content to be displayed.
       *text_file*
            type: String (optional)
            File path.
       *word_wrap*
            type: boolean (optional)
            Word wrap.
    """

    def __init__(self, source, color1=None, outline=None, text_file=None, word_wrap=None, color2=None, log_mode=None, from_file=None, custom_width=None, font=None, text=None, drop_shadow=None):
        Baserequests.__init__(self)
        self.name = 'SetTextFreetype2Properties'
        self.dataout['source'] = source
        self.dataout['color1'] = color1
        self.dataout['outline'] = outline
        self.dataout['text_file'] = text_file
        self.dataout['word_wrap'] = word_wrap
        self.dataout['color2'] = color2
        self.dataout['log_mode'] = log_mode
        self.dataout['from_file'] = from_file
        self.dataout['custom_width'] = custom_width
        self.dataout['font'] = font
        self.dataout['text'] = text
        self.dataout['drop_shadow'] = drop_shadow


class GetBrowserSourceProperties(Baserequests):
    """Get current properties for a Browser Source.

    :Arguments:
       *source*
            type: String
            Source name.
    :Returns:
       *source*
            type: String
            Source name.
       *is_local_file*
            type: boolean
            Indicates that a local file is in use.
       *local_file*
            type: String
            file path.
       *url*
            type: String
            Url.
       *css*
            type: String
            CSS to inject.
       *width*
            type: int
            Width.
       *height*
            type: int
            Height.
       *fps*
            type: int
            Framerate.
       *shutdown*
            type: boolean
            Indicates whether the source should be shutdown when not visible.
    """

    def __init__(self, source):
        Baserequests.__init__(self)
        self.name = 'GetBrowserSourceProperties'
        self.datain['css'] = None
        self.datain['is_local_file'] = None
        self.datain['shutdown'] = None
        self.datain['url'] = None
        self.datain['fps'] = None
        self.datain['source'] = None
        self.datain['width'] = None
        self.datain['height'] = None
        self.datain['local_file'] = None
        self.dataout['source'] = source

    def getCss(self):
        return self.datain['css']

    def getIs_local_file(self):
        return self.datain['is_local_file']

    def getShutdown(self):
        return self.datain['shutdown']

    def getUrl(self):
        return self.datain['url']

    def getFps(self):
        return self.datain['fps']

    def getSource(self):
        return self.datain['source']

    def getWidth(self):
        return self.datain['width']

    def getHeight(self):
        return self.datain['height']

    def getLocal_file(self):
        return self.datain['local_file']


class SetBrowserSourceProperties(Baserequests):
    """Set current properties for a Browser Source.

    :Arguments:
       *source*
            type: String
            Name of the source.
       *is_local_file*
            type: boolean (optional)
            Indicates that a local file is in use.
       *local_file*
            type: String (optional)
            file path.
       *url*
            type: String (optional)
            Url.
       *css*
            type: String (optional)
            CSS to inject.
       *width*
            type: int (optional)
            Width.
       *height*
            type: int (optional)
            Height.
       *fps*
            type: int (optional)
            Framerate.
       *shutdown*
            type: boolean (optional)
            Indicates whether the source should be shutdown when not visible.
       *render*
            type: boolean (optional)
            Visibility of the scene item.
    """

    def __init__(self, source, is_local_file=None, css=None, fps=None, url=None, local_file=None, width=None, height=None, shutdown=None, render=None):
        Baserequests.__init__(self)
        self.name = 'SetBrowserSourceProperties'
        self.dataout['source'] = source
        self.dataout['is_local_file'] = is_local_file
        self.dataout['css'] = css
        self.dataout['fps'] = fps
        self.dataout['url'] = url
        self.dataout['local_file'] = local_file
        self.dataout['width'] = width
        self.dataout['height'] = height
        self.dataout['shutdown'] = shutdown
        self.dataout['render'] = render


class GetSpecialSources(Baserequests):
    """Get configured special sources like Desktop Audio and Mic/Aux sources.

    :Returns:
       *desktop_1*
            type: String (optional)
            Name of the first Desktop Audio capture source.
       *desktop_2*
            type: String (optional)
            Name of the second Desktop Audio capture source.
       *mic_1*
            type: String (optional)
            Name of the first Mic/Aux input source.
       *mic_2*
            type: String (optional)
            Name of the second Mic/Aux input source.
       *mic_3*
            type: String (optional)
            NAme of the third Mic/Aux input source.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetSpecialSources'
        self.datain['desktop-2'] = None
        self.datain['desktop-1'] = None
        self.datain['mic-3'] = None
        self.datain['mic-1'] = None
        self.datain['mic-2'] = None

    def getDesktop2(self):
        return self.datain['desktop-2']

    def getDesktop1(self):
        return self.datain['desktop-1']

    def getMic3(self):
        return self.datain['mic-3']

    def getMic1(self):
        return self.datain['mic-1']

    def getMic2(self):
        return self.datain['mic-2']


class GetSourceFilters(Baserequests):
    """List filters applied to a source

    :Arguments:
       *sourceName*
            type: String
            Source name
    :Returns:
       *filters*
            type: Array<Object>
            List of filters for the specified source
       *filters.*.enabled*
            type: Boolean
            Filter status (enabled or not)
       *filters.*.type*
            type: String
            Filter type
       *filters.*.name*
            type: String
            Filter name
       *filters.*.settings*
            type: Object
            Filter settings
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetSourceFilters'
        self.datain['filters'] = None
        self.dataout['sourceName'] = sourceName

    def getFilters(self):
        return self.datain['filters']


class GetSourceFilterInfo(Baserequests):
    """List filters applied to a source

    :Arguments:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Source filter name
    :Returns:
       *enabled*
            type: Boolean
            Filter status (enabled or not)
       *type*
            type: String
            Filter type
       *name*
            type: String
            Filter name
       *settings*
            type: Object
            Filter settings
    """

    def __init__(self, filterName, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetSourceFilterInfo'
        self.datain['name'] = None
        self.datain['enabled'] = None
        self.datain['type'] = None
        self.datain['settings'] = None
        self.dataout['filterName'] = filterName
        self.dataout['sourceName'] = sourceName

    def getName(self):
        return self.datain['name']

    def getEnabled(self):
        return self.datain['enabled']

    def getType(self):
        return self.datain['type']

    def getSettings(self):
        return self.datain['settings']


class AddFilterToSource(Baserequests):
    """Add a new filter to a source. Available source types along with their settings properties are available from `GetSourceTypesList`.

    :Arguments:
       *sourceName*
            type: String
            Name of the source on which the filter is added
       *filterName*
            type: String
            Name of the new filter
       *filterType*
            type: String
            Filter type
       *filterSettings*
            type: Object
            Filter settings
    """

    def __init__(self, filterName, filterSettings, sourceName, filterType):
        Baserequests.__init__(self)
        self.name = 'AddFilterToSource'
        self.dataout['filterName'] = filterName
        self.dataout['filterSettings'] = filterSettings
        self.dataout['sourceName'] = sourceName
        self.dataout['filterType'] = filterType


class RemoveFilterFromSource(Baserequests):
    """Remove a filter from a source

    :Arguments:
       *sourceName*
            type: String
            Name of the source from which the specified filter is removed
       *filterName*
            type: String
            Name of the filter to remove
    """

    def __init__(self, filterName, sourceName):
        Baserequests.__init__(self)
        self.name = 'RemoveFilterFromSource'
        self.dataout['filterName'] = filterName
        self.dataout['sourceName'] = sourceName


class ReorderSourceFilter(Baserequests):
    """Move a filter in the chain (absolute index positioning)

    :Arguments:
       *sourceName*
            type: String
            Name of the source to which the filter belongs
       *filterName*
            type: String
            Name of the filter to reorder
       *newIndex*
            type: Integer
            Desired position of the filter in the chain
    """

    def __init__(self, filterName, newIndex, sourceName):
        Baserequests.__init__(self)
        self.name = 'ReorderSourceFilter'
        self.dataout['filterName'] = filterName
        self.dataout['newIndex'] = newIndex
        self.dataout['sourceName'] = sourceName


class MoveSourceFilter(Baserequests):
    """Move a filter in the chain (relative positioning)

    :Arguments:
       *sourceName*
            type: String
            Name of the source to which the filter belongs
       *filterName*
            type: String
            Name of the filter to reorder
       *movementType*
            type: String
            How to move the filter around in the source's filter chain. Either "up", "down", "top" or "bottom".
    """

    def __init__(self, filterName, movementType, sourceName):
        Baserequests.__init__(self)
        self.name = 'MoveSourceFilter'
        self.dataout['filterName'] = filterName
        self.dataout['movementType'] = movementType
        self.dataout['sourceName'] = sourceName


class SetSourceFilterSettings(Baserequests):
    """Update settings of a filter

    :Arguments:
       *sourceName*
            type: String
            Name of the source to which the filter belongs
       *filterName*
            type: String
            Name of the filter to reconfigure
       *filterSettings*
            type: Object
            New settings. These will be merged to the current filter settings.
    """

    def __init__(self, filterName, filterSettings, sourceName):
        Baserequests.__init__(self)
        self.name = 'SetSourceFilterSettings'
        self.dataout['filterName'] = filterName
        self.dataout['filterSettings'] = filterSettings
        self.dataout['sourceName'] = sourceName


class SetSourceFilterVisibility(Baserequests):
    """Change the visibility/enabled state of a filter

    :Arguments:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Source filter name
       *filterEnabled*
            type: Boolean
            New filter state
    """

    def __init__(self, filterName, filterEnabled, sourceName):
        Baserequests.__init__(self)
        self.name = 'SetSourceFilterVisibility'
        self.dataout['filterName'] = filterName
        self.dataout['filterEnabled'] = filterEnabled
        self.dataout['sourceName'] = sourceName


class GetAudioMonitorType(Baserequests):
    """Get the audio monitoring type of the specified source.

    :Arguments:
       *sourceName*
            type: String
            Source name.
    :Returns:
       *monitorType*
            type: String
            The monitor type in use. Options: `none`, `monitorOnly`, `monitorAndOutput`.
    """

    def __init__(self, sourceName):
        Baserequests.__init__(self)
        self.name = 'GetAudioMonitorType'
        self.datain['monitorType'] = None
        self.dataout['sourceName'] = sourceName

    def getMonitortype(self):
        return self.datain['monitorType']


class SetAudioMonitorType(Baserequests):
    """Set the audio monitoring type of the specified source.

    :Arguments:
       *sourceName*
            type: String
            Source name.
       *monitorType*
            type: String
            The monitor type to use. Options: `none`, `monitorOnly`, `monitorAndOutput`.
    """

    def __init__(self, monitorType, sourceName):
        Baserequests.__init__(self)
        self.name = 'SetAudioMonitorType'
        self.dataout['monitorType'] = monitorType
        self.dataout['sourceName'] = sourceName


class TakeSourceScreenshot(Baserequests):
    """

At least `embedPictureFormat` or `saveToFilePath` must be specified.

Clients can specify `width` and `height` parameters to receive scaled pictures. Aspect ratio is
preserved if only one of these two parameters is specified.

    :Arguments:
       *sourceName*
            type: String (optional)
            Source name. Note that, since scenes are also sources, you can also provide a scene name. If not provided, the currently active scene is used.
       *embedPictureFormat*
            type: String (optional)
            Format of the Data URI encoded picture. Can be "png", "jpg", "jpeg" or "bmp" (or any other value supported by Qt's Image module)
       *saveToFilePath*
            type: String (optional)
            Full file path (file extension included) where the captured image is to be saved. Can be in a format different from `pictureFormat`. Can be a relative path.
       *fileFormat*
            type: String (optional)
            Format to save the image file as (one of the values provided in the `supported-image-export-formats` response field of `GetVersion`). If not specified, tries to guess based on file extension.
       *compressionQuality*
            type: int (optional)
            Compression ratio between -1 and 100 to write the image with. -1 is automatic, 1 is smallest file/most compression, 100 is largest file/least compression. Varies with image type.
       *width*
            type: int (optional)
            Screenshot width. Defaults to the source's base width.
       *height*
            type: int (optional)
            Screenshot height. Defaults to the source's base height.
    :Returns:
       *sourceName*
            type: String
            Source name
       *img*
            type: String
            Image Data URI (if `embedPictureFormat` was specified in the request)
       *imageFile*
            type: String
            Absolute path to the saved image file (if `saveToFilePath` was specified in the request)
    """

    def __init__(self, saveToFilePath=None, sourceName=None, compressionQuality=None, fileFormat=None, width=None, height=None, embedPictureFormat=None):
        Baserequests.__init__(self)
        self.name = 'TakeSourceScreenshot'
        self.datain['img'] = None
        self.datain['sourceName'] = None
        self.datain['imageFile'] = None
        self.dataout['saveToFilePath'] = saveToFilePath
        self.dataout['sourceName'] = sourceName
        self.dataout['compressionQuality'] = compressionQuality
        self.dataout['fileFormat'] = fileFormat
        self.dataout['width'] = width
        self.dataout['height'] = height
        self.dataout['embedPictureFormat'] = embedPictureFormat

    def getImg(self):
        return self.datain['img']

    def getSourcename(self):
        return self.datain['sourceName']

    def getImagefile(self):
        return self.datain['imageFile']


class ListOutputs(Baserequests):
    """List existing outputs

    :Returns:
       *outputs*
            type: Array<Output>
            Outputs list
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'ListOutputs'
        self.datain['outputs'] = None

    def getOutputs(self):
        return self.datain['outputs']


class GetOutputInfo(Baserequests):
    """Get information about a single output

    :Arguments:
       *outputName*
            type: String
            Output name
    :Returns:
       *outputInfo*
            type: Output
            Output info
    """

    def __init__(self, outputName):
        Baserequests.__init__(self)
        self.name = 'GetOutputInfo'
        self.datain['outputInfo'] = None
        self.dataout['outputName'] = outputName

    def getOutputinfo(self):
        return self.datain['outputInfo']


class StartOutput(Baserequests):
    """

Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not function properly when they are controlled in this way.

    :Arguments:
       *outputName*
            type: String
            Output name
    """

    def __init__(self, outputName):
        Baserequests.__init__(self)
        self.name = 'StartOutput'
        self.dataout['outputName'] = outputName


class StopOutput(Baserequests):
    """

Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not function properly when they are controlled in this way.

    :Arguments:
       *outputName*
            type: String
            Output name
       *force*
            type: boolean (optional)
            Force stop (default: false)
    """

    def __init__(self, outputName, force=None):
        Baserequests.__init__(self)
        self.name = 'StopOutput'
        self.dataout['outputName'] = outputName
        self.dataout['force'] = force


class SetCurrentProfile(Baserequests):
    """Set the currently active profile.

    :Arguments:
       *profile_name*
            type: String
            Name of the desired profile.
    """

    def __init__(self, profile_name):
        Baserequests.__init__(self)
        self.name = 'SetCurrentProfile'
        self.dataout['profile-name'] = profile_name


class GetCurrentProfile(Baserequests):
    """Get the name of the current profile.

    :Returns:
       *profile_name*
            type: String
            Name of the currently active profile.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetCurrentProfile'
        self.datain['profile-name'] = None

    def getProfileName(self):
        return self.datain['profile-name']


class ListProfiles(Baserequests):
    """Get a list of available profiles.

    :Returns:
       *profiles*
            type: Array<Object>
            List of available profiles.
       *profiles.*.profile_name*
            type: String
            Filter name
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'ListProfiles'
        self.datain['profiles'] = None

    def getProfiles(self):
        return self.datain['profiles']


class GetRecordingStatus(Baserequests):
    """Get current recording status.

    :Returns:
       *isRecording*
            type: boolean
            Current recording status.
       *isRecordingPaused*
            type: boolean
            Whether the recording is paused or not.
       *recordTimecode*
            type: String (optional)
            Time elapsed since recording started (only present if currently recording).
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetRecordingStatus'
        self.datain['isRecordingPaused'] = None
        self.datain['isRecording'] = None
        self.datain['recordTimecode'] = None

    def getIsrecordingpaused(self):
        return self.datain['isRecordingPaused']

    def getIsrecording(self):
        return self.datain['isRecording']

    def getRecordtimecode(self):
        return self.datain['recordTimecode']


class StartStopRecording(Baserequests):
    """Toggle recording on or off (depending on the current recording state).

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StartStopRecording'


class StartRecording(Baserequests):
    """Start recording.
Will return an `error` if recording is already active.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StartRecording'


class StopRecording(Baserequests):
    """Stop recording.
Will return an `error` if recording is not active.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StopRecording'


class PauseRecording(Baserequests):
    """Pause the current recording.
Returns an error if recording is not active or already paused.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'PauseRecording'


class ResumeRecording(Baserequests):
    """Resume/unpause the current recording (if paused).
Returns an error if recording is not active or not paused.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'ResumeRecording'


class SetRecordingFolder(Baserequests):
    """

Please note: if `SetRecordingFolder` is called while a recording is
in progress, the change won't be applied immediately and will be
effective on the next recording.

    :Arguments:
       *rec_folder*
            type: String
            Path of the recording folder.
    """

    def __init__(self, rec_folder):
        Baserequests.__init__(self)
        self.name = 'SetRecordingFolder'
        self.dataout['rec-folder'] = rec_folder


class GetRecordingFolder(Baserequests):
    """Get the path of  the current recording folder.

    :Returns:
       *rec_folder*
            type: String
            Path of the recording folder.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetRecordingFolder'
        self.datain['rec-folder'] = None

    def getRecFolder(self):
        return self.datain['rec-folder']


class GetReplayBufferStatus(Baserequests):
    """Get the status of the OBS replay buffer.

    :Returns:
       *isReplayBufferActive*
            type: boolean
            Current recording status.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetReplayBufferStatus'
        self.datain['isReplayBufferActive'] = None

    def getIsreplaybufferactive(self):
        return self.datain['isReplayBufferActive']


class StartStopReplayBuffer(Baserequests):
    """Toggle the Replay Buffer on/off (depending on the current state of the replay buffer).

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StartStopReplayBuffer'


class StartReplayBuffer(Baserequests):
    """Start recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is already active or if the
"Save Replay Buffer" hotkey is not set in OBS' settings.
Setting this hotkey is mandatory, even when triggering saves only
through obs-websocket.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StartReplayBuffer'


class StopReplayBuffer(Baserequests):
    """Stop recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is not active.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StopReplayBuffer'


class SaveReplayBuffer(Baserequests):
    """Flush and save the contents of the Replay Buffer to disk. This is
basically the same as triggering the "Save Replay Buffer" hotkey.
Will return an `error` if the Replay Buffer is not active.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'SaveReplayBuffer'


class SetCurrentSceneCollection(Baserequests):
    """Change the active scene collection.

    :Arguments:
       *sc_name*
            type: String
            Name of the desired scene collection.
    """

    def __init__(self, sc_name):
        Baserequests.__init__(self)
        self.name = 'SetCurrentSceneCollection'
        self.dataout['sc-name'] = sc_name


class GetCurrentSceneCollection(Baserequests):
    """Get the name of the current scene collection.

    :Returns:
       *sc_name*
            type: String
            Name of the currently active scene collection.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetCurrentSceneCollection'
        self.datain['sc-name'] = None

    def getScName(self):
        return self.datain['sc-name']


class ListSceneCollections(Baserequests):
    """List available scene collections

    :Returns:
       *scene_collections*
            type: Array<String>
            Scene collections list
       *scene_collections.*.sc_name*
            type: String
            Scene collection name
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'ListSceneCollections'
        self.datain['scene-collections'] = None

    def getSceneCollections(self):
        return self.datain['scene-collections']


class GetSceneItemList(Baserequests):
    """Get a list of all scene items in a scene.

    :Arguments:
       *sceneName*
            type: String (optional)
            Name of the scene to get the list of scene items from. Defaults to the current scene if not specified.
    :Returns:
       *sceneName*
            type: String
            Name of the requested (or current) scene
       *sceneItems*
            type: Array<Object>
            Array of scene items
       *sceneItems.*.itemId*
            type: int
            Unique item id of the source item
       *sceneItems.*.sourceKind*
            type: String
            ID if the scene item's source. For example `vlc_source` or `image_source`
       *sceneItems.*.sourceName*
            type: String
            Name of the scene item's source
       *sceneItems.*.sourceType*
            type: String
            Type of the scene item's source. Either `input`, `group`, or `scene`
    """

    def __init__(self, sceneName=None):
        Baserequests.__init__(self)
        self.name = 'GetSceneItemList'
        self.datain['sceneItems'] = None
        self.datain['sceneName'] = None
        self.dataout['sceneName'] = sceneName

    def getSceneitems(self):
        return self.datain['sceneItems']

    def getScenename(self):
        return self.datain['sceneName']


class GetSceneItemProperties(Baserequests):
    """Gets the scene specific properties of the specified source item.
Coordinates are relative to the item's parent (the scene or group it belongs to).

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
       *item.name*
            type: String (optional)
            Scene Item name (if the `item` field is an object)
       *item.id*
            type: int (optional)
            Scene Item ID (if the `item` field is an object)
    :Returns:
       *name*
            type: String
            Scene Item name.
       *itemId*
            type: int
            Scene Item ID.
       *position.x*
            type: double
            The x position of the source from the left.
       *position.y*
            type: double
            The y position of the source from the top.
       *position.alignment*
            type: int
            The point on the source that the item is manipulated from.
       *rotation*
            type: double
            The clockwise rotation of the item in degrees around the point of alignment.
       *scale.x*
            type: double
            The x-scale factor of the source.
       *scale.y*
            type: double
            The y-scale factor of the source.
       *crop.top*
            type: int
            The number of pixels cropped off the top of the source before scaling.
       *crop.right*
            type: int
            The number of pixels cropped off the right of the source before scaling.
       *crop.bottom*
            type: int
            The number of pixels cropped off the bottom of the source before scaling.
       *crop.left*
            type: int
            The number of pixels cropped off the left of the source before scaling.
       *visible*
            type: bool
            If the source is visible.
       *muted*
            type: bool
            If the source is muted.
       *locked*
            type: bool
            If the source's transform is locked.
       *bounds.type*
            type: String
            Type of bounding box. Can be "OBS_BOUNDS_STRETCH", "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT", "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
       *bounds.alignment*
            type: int
            Alignment of the bounding box.
       *bounds.x*
            type: double
            Width of the bounding box.
       *bounds.y*
            type: double
            Height of the bounding box.
       *sourceWidth*
            type: int
            Base width (without scaling) of the source
       *sourceHeight*
            type: int
            Base source (without scaling) of the source
       *width*
            type: double
            Scene item width (base source width multiplied by the horizontal scaling factor)
       *height*
            type: double
            Scene item height (base source height multiplied by the vertical scaling factor)
       *alignment*
            type: int
            The point on the source that the item is manipulated from. The sum of 1=Left or 2=Right, and 4=Top or 8=Bottom, or omit to center on that axis.
       *parentGroupName*
            type: String (optional)
            Name of the item's parent (if this item belongs to a group)
       *groupChildren*
            type: Array<SceneItemTransform> (optional)
            List of children (if this item is a group)
    """

    def __init__(self, item, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'GetSceneItemProperties'
        self.datain['itemId'] = None
        self.datain['crop'] = None
        self.datain['scale'] = None
        self.datain['rotation'] = None
        self.datain['sourceWidth'] = None
        self.datain['groupChildren'] = None
        self.datain['sourceHeight'] = None
        self.datain['width'] = None
        self.datain['visible'] = None
        self.datain['bounds'] = None
        self.datain['height'] = None
        self.datain['locked'] = None
        self.datain['position'] = None
        self.datain['name'] = None
        self.datain['muted'] = None
        self.datain['alignment'] = None
        self.datain['parentGroupName'] = None
        self.dataout['item'] = item
        self.dataout['scene-name'] = scene_name

    def getItemid(self):
        return self.datain['itemId']

    def getCrop(self):
        return self.datain['crop']

    def getScale(self):
        return self.datain['scale']

    def getRotation(self):
        return self.datain['rotation']

    def getSourcewidth(self):
        return self.datain['sourceWidth']

    def getGroupchildren(self):
        return self.datain['groupChildren']

    def getSourceheight(self):
        return self.datain['sourceHeight']

    def getWidth(self):
        return self.datain['width']

    def getVisible(self):
        return self.datain['visible']

    def getBounds(self):
        return self.datain['bounds']

    def getHeight(self):
        return self.datain['height']

    def getLocked(self):
        return self.datain['locked']

    def getPosition(self):
        return self.datain['position']

    def getName(self):
        return self.datain['name']

    def getMuted(self):
        return self.datain['muted']

    def getAlignment(self):
        return self.datain['alignment']

    def getParentgroupname(self):
        return self.datain['parentGroupName']


class SetSceneItemProperties(Baserequests):
    """Sets the scene specific properties of a source. Unspecified properties will remain unchanged.
Coordinates are relative to the item's parent (the scene or group it belongs to).

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the source item belongs to. Defaults to the current scene.
       *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
       *item.name*
            type: String (optional)
            Scene Item name (if the `item` field is an object)
       *item.id*
            type: int (optional)
            Scene Item ID (if the `item` field is an object)
       *position.x*
            type: double (optional)
            The new x position of the source.
       *position.y*
            type: double (optional)
            The new y position of the source.
       *position.alignment*
            type: int (optional)
            The new alignment of the source.
       *rotation*
            type: double (optional)
            The new clockwise rotation of the item in degrees.
       *scale.x*
            type: double (optional)
            The new x scale of the item.
       *scale.y*
            type: double (optional)
            The new y scale of the item.
       *crop.top*
            type: int (optional)
            The new amount of pixels cropped off the top of the source before scaling.
       *crop.bottom*
            type: int (optional)
            The new amount of pixels cropped off the bottom of the source before scaling.
       *crop.left*
            type: int (optional)
            The new amount of pixels cropped off the left of the source before scaling.
       *crop.right*
            type: int (optional)
            The new amount of pixels cropped off the right of the source before scaling.
       *visible*
            type: bool (optional)
            The new visibility of the source. 'true' shows source, 'false' hides source.
       *locked*
            type: bool (optional)
            The new locked status of the source. 'true' keeps it in its current position, 'false' allows movement.
       *bounds.type*
            type: String (optional)
            The new bounds type of the source. Can be "OBS_BOUNDS_STRETCH", "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT", "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
       *bounds.alignment*
            type: int (optional)
            The new alignment of the bounding box. (0-2, 4-6, 8-10)
       *bounds.x*
            type: double (optional)
            The new width of the bounding box.
       *bounds.y*
            type: double (optional)
            The new height of the bounding box.
    """

    def __init__(self, item, position=None, crop=None, scale=None, rotation=None, bounds=None, locked=None, visible=None, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'SetSceneItemProperties'
        self.dataout['item'] = item
        self.dataout['position'] = position
        self.dataout['crop'] = crop
        self.dataout['scale'] = scale
        self.dataout['rotation'] = rotation
        self.dataout['bounds'] = bounds
        self.dataout['locked'] = locked
        self.dataout['visible'] = visible
        self.dataout['scene-name'] = scene_name


class ResetSceneItem(Baserequests):
    """Reset a scene item.

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
       *item.name*
            type: String (optional)
            Scene Item name (if the `item` field is an object)
       *item.id*
            type: int (optional)
            Scene Item ID (if the `item` field is an object)
    """

    def __init__(self, item, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'ResetSceneItem'
        self.dataout['item'] = item
        self.dataout['scene-name'] = scene_name


class SetSceneItemRender(Baserequests):
    """Show or hide a specified source item in a specified scene.

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the currently active scene.
       *source*
            type: String
            Scene Item name.
       *render*
            type: boolean
            true = shown ; false = hidden
    """

    def __init__(self, render, source, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'SetSceneItemRender'
        self.dataout['render'] = render
        self.dataout['source'] = source
        self.dataout['scene-name'] = scene_name


class SetSceneItemPosition(Baserequests):
    """Sets the coordinates of a specified source item.

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: String
            Scene Item name.
       *x*
            type: double
            X coordinate.
       *y*
            type: double
            Y coordinate.
    """

    def __init__(self, item, y, x, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'SetSceneItemPosition'
        self.dataout['item'] = item
        self.dataout['y'] = y
        self.dataout['x'] = x
        self.dataout['scene-name'] = scene_name


class SetSceneItemTransform(Baserequests):
    """Set the transform of the specified source item.

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: String
            Scene Item name.
       *x_scale*
            type: double
            Width scale factor.
       *y_scale*
            type: double
            Height scale factor.
       *rotation*
            type: double
            Source item rotation (in degrees).
    """

    def __init__(self, item, rotation, y_scale, x_scale, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'SetSceneItemTransform'
        self.dataout['item'] = item
        self.dataout['rotation'] = rotation
        self.dataout['y-scale'] = y_scale
        self.dataout['x-scale'] = x_scale
        self.dataout['scene-name'] = scene_name


class SetSceneItemCrop(Baserequests):
    """Sets the crop coordinates of the specified source item.

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: String
            Scene Item name.
       *top*
            type: int
            Pixel position of the top of the source item.
       *bottom*
            type: int
            Pixel position of the bottom of the source item.
       *left*
            type: int
            Pixel position of the left of the source item.
       *right*
            type: int
            Pixel position of the right of the source item.
    """

    def __init__(self, right, top, bottom, item, left, scene_name=None):
        Baserequests.__init__(self)
        self.name = 'SetSceneItemCrop'
        self.dataout['right'] = right
        self.dataout['top'] = top
        self.dataout['bottom'] = bottom
        self.dataout['item'] = item
        self.dataout['left'] = left
        self.dataout['scene-name'] = scene_name


class DeleteSceneItem(Baserequests):
    """Deletes a scene item.

    :Arguments:
       *scene*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: Object
            Scene item to delete (required)
       *item.name*
            type: String
            Scene Item name (prefer `id`, including both is acceptable).
       *item.id*
            type: int
            Scene Item ID.
    """

    def __init__(self, item, scene=None):
        Baserequests.__init__(self)
        self.name = 'DeleteSceneItem'
        self.dataout['item'] = item
        self.dataout['scene'] = scene


class AddSceneItem(Baserequests):
    """Creates a scene item in a scene. In other words, this is how you add a source into a scene.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to create the scene item in
       *sourceName*
            type: String
            Name of the source to be added
       *setVisible*
            type: boolean
            Whether to make the sceneitem visible on creation or not. Default `true`
    :Returns:
       *itemId*
            type: int
            Numerical ID of the created scene item
    """

    def __init__(self, setVisible, sceneName, sourceName):
        Baserequests.__init__(self)
        self.name = 'AddSceneItem'
        self.datain['itemId'] = None
        self.dataout['setVisible'] = setVisible
        self.dataout['sceneName'] = sceneName
        self.dataout['sourceName'] = sourceName

    def getItemid(self):
        return self.datain['itemId']


class DuplicateSceneItem(Baserequests):
    """Duplicates a scene item.

    :Arguments:
       *fromScene*
            type: String (optional)
            Name of the scene to copy the item from. Defaults to the current scene.
       *toScene*
            type: String (optional)
            Name of the scene to create the item in. Defaults to the current scene.
       *item*
            type: Object
            Scene Item to duplicate from the source scene (required)
       *item.name*
            type: String
            Scene Item name (prefer `id`, including both is acceptable).
       *item.id*
            type: int
            Scene Item ID.
    :Returns:
       *scene*
            type: String
            Name of the scene where the new item was created
       *item*
            type: Object
            New item info
       *item.id*
            type: int
            New item ID
       *item.name*
            type: String
            New item name
    """

    def __init__(self, item, fromScene=None, toScene=None):
        Baserequests.__init__(self)
        self.name = 'DuplicateSceneItem'
        self.datain['item'] = None
        self.datain['scene'] = None
        self.dataout['item'] = item
        self.dataout['fromScene'] = fromScene
        self.dataout['toScene'] = toScene

    def getItem(self):
        return self.datain['item']

    def getScene(self):
        return self.datain['scene']


class SetCurrentScene(Baserequests):
    """Switch to the specified scene.

    :Arguments:
       *scene_name*
            type: String
            Name of the scene to switch to.
    """

    def __init__(self, scene_name):
        Baserequests.__init__(self)
        self.name = 'SetCurrentScene'
        self.dataout['scene-name'] = scene_name


class GetCurrentScene(Baserequests):
    """Get the current scene's name and source items.

    :Returns:
       *name*
            type: String
            Name of the currently active scene.
       *sources*
            type: Array<SceneItem>
            Ordered list of the current scene's source items.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetCurrentScene'
        self.datain['sources'] = None
        self.datain['name'] = None

    def getSources(self):
        return self.datain['sources']

    def getName(self):
        return self.datain['name']


class GetSceneList(Baserequests):
    """Get a list of scenes in the currently active profile.

    :Returns:
       *current_scene*
            type: String
            Name of the currently active scene.
       *scenes*
            type: Array<Scene>
            Ordered list of the current profile's scenes (See [GetCurrentScene](#getcurrentscene) for more information).
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetSceneList'
        self.datain['current-scene'] = None
        self.datain['scenes'] = None

    def getCurrentScene(self):
        return self.datain['current-scene']

    def getScenes(self):
        return self.datain['scenes']


class CreateScene(Baserequests):
    """Create a new scene scene.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to create.
    """

    def __init__(self, sceneName):
        Baserequests.__init__(self)
        self.name = 'CreateScene'
        self.dataout['sceneName'] = sceneName


class ReorderSceneItems(Baserequests):
    """Changes the order of scene items in the requested scene.

    :Arguments:
       *scene*
            type: String (optional)
            Name of the scene to reorder (defaults to current).
       *items*
            type: Array<Scene>
            Ordered list of objects with name and/or id specified. Id preferred due to uniqueness per scene
       *items.*.id*
            type: int (optional)
            Id of a specific scene item. Unique on a scene by scene basis.
       *items.*.name*
            type: String (optional)
            Name of a scene item. Sufficiently unique if no scene items share sources within the scene.
    """

    def __init__(self, items, scene=None):
        Baserequests.__init__(self)
        self.name = 'ReorderSceneItems'
        self.dataout['items'] = items
        self.dataout['scene'] = scene


class SetSceneTransitionOverride(Baserequests):
    """Set a scene to use a specific transition override.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to switch to.
       *transitionName*
            type: String
            Name of the transition to use.
       *transitionDuration*
            type: int (Optional)
            Duration in milliseconds of the transition if transition is not fixed. Defaults to the current duration specified in the UI if there is no current override and this value is not given.
    """

    def __init__(self, transitionDuration, sceneName, transitionName):
        Baserequests.__init__(self)
        self.name = 'SetSceneTransitionOverride'
        self.dataout['transitionDuration'] = transitionDuration
        self.dataout['sceneName'] = sceneName
        self.dataout['transitionName'] = transitionName


class RemoveSceneTransitionOverride(Baserequests):
    """Remove any transition override on a scene.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to switch to.
    """

    def __init__(self, sceneName):
        Baserequests.__init__(self)
        self.name = 'RemoveSceneTransitionOverride'
        self.dataout['sceneName'] = sceneName


class GetSceneTransitionOverride(Baserequests):
    """Get the current scene transition override.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to switch to.
    :Returns:
       *transitionName*
            type: String
            Name of the current overriding transition. Empty string if no override is set.
       *transitionDuration*
            type: int
            Transition duration. `-1` if no override is set.
    """

    def __init__(self, sceneName):
        Baserequests.__init__(self)
        self.name = 'GetSceneTransitionOverride'
        self.datain['transitionDuration'] = None
        self.datain['transitionName'] = None
        self.dataout['sceneName'] = sceneName

    def getTransitionduration(self):
        return self.datain['transitionDuration']

    def getTransitionname(self):
        return self.datain['transitionName']


class GetStreamingStatus(Baserequests):
    """Get current streaming and recording status.

    :Returns:
       *streaming*
            type: boolean
            Current streaming status.
       *recording*
            type: boolean
            Current recording status.
       *stream_timecode*
            type: String (optional)
            Time elapsed since streaming started (only present if currently streaming).
       *rec_timecode*
            type: String (optional)
            Time elapsed since recording started (only present if currently recording).
       *preview_only*
            type: boolean
            Always false. Retrocompatibility with OBSRemote.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetStreamingStatus'
        self.datain['rec-timecode'] = None
        self.datain['streaming'] = None
        self.datain['preview-only'] = None
        self.datain['stream-timecode'] = None
        self.datain['recording'] = None

    def getRecTimecode(self):
        return self.datain['rec-timecode']

    def getStreaming(self):
        return self.datain['streaming']

    def getPreviewOnly(self):
        return self.datain['preview-only']

    def getStreamTimecode(self):
        return self.datain['stream-timecode']

    def getRecording(self):
        return self.datain['recording']


class StartStopStreaming(Baserequests):
    """Toggle streaming on or off (depending on the current stream state).

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StartStopStreaming'


class StartStreaming(Baserequests):
    """Start streaming.
Will return an `error` if streaming is already active.

    :Arguments:
       *stream*
            type: Object (optional)
            Special stream configuration. Please note: these won't be saved to OBS' configuration.
       *stream.type*
            type: String (optional)
            If specified ensures the type of stream matches the given type (usually 'rtmp_custom' or 'rtmp_common'). If the currently configured stream type does not match the given stream type, all settings must be specified in the `settings` object or an error will occur when starting the stream.
       *stream.metadata*
            type: Object (optional)
            Adds the given object parameters as encoded query string parameters to the 'key' of the RTMP stream. Used to pass data to the RTMP service about the streaming. May be any String, Numeric, or Boolean field.
       *stream.settings*
            type: Object (optional)
            Settings for the stream.
       *stream.settings.server*
            type: String (optional)
            The publish URL.
       *stream.settings.key*
            type: String (optional)
            The publish key of the stream.
       *stream.settings.use_auth*
            type: boolean (optional)
            Indicates whether authentication should be used when connecting to the streaming server.
       *stream.settings.username*
            type: String (optional)
            If authentication is enabled, the username for the streaming server. Ignored if `use_auth` is not set to `true`.
       *stream.settings.password*
            type: String (optional)
            If authentication is enabled, the password for the streaming server. Ignored if `use_auth` is not set to `true`.
    """

    def __init__(self, stream=None):
        Baserequests.__init__(self)
        self.name = 'StartStreaming'
        self.dataout['stream'] = stream


class StopStreaming(Baserequests):
    """Stop streaming.
Will return an `error` if streaming is not active.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'StopStreaming'


class SetStreamSettings(Baserequests):
    """Sets one or more attributes of the current streaming server settings. Any options not passed will remain unchanged. Returns the updated settings in response. If 'type' is different than the current streaming service type, all settings are required. Returns the full settings of the stream (the same as GetStreamSettings).

    :Arguments:
       *type*
            type: String
            The type of streaming service configuration, usually `rtmp_custom` or `rtmp_common`.
       *settings*
            type: Object
            The actual settings of the stream.
       *settings.server*
            type: String (optional)
            The publish URL.
       *settings.key*
            type: String (optional)
            The publish key.
       *settings.use_auth*
            type: boolean (optional)
            Indicates whether authentication should be used when connecting to the streaming server.
       *settings.username*
            type: String (optional)
            The username for the streaming service.
       *settings.password*
            type: String (optional)
            The password for the streaming service.
       *save*
            type: boolean
            Persist the settings to disk.
    """

    def __init__(self, type, settings, save):
        Baserequests.__init__(self)
        self.name = 'SetStreamSettings'
        self.dataout['type'] = type
        self.dataout['settings'] = settings
        self.dataout['save'] = save


class GetStreamSettings(Baserequests):
    """Get the current streaming server settings.

    :Returns:
       *type*
            type: String
            The type of streaming service configuration. Possible values: 'rtmp_custom' or 'rtmp_common'.
       *settings*
            type: Object
            Stream settings object.
       *settings.server*
            type: String
            The publish URL.
       *settings.key*
            type: String
            The publish key of the stream.
       *settings.use_auth*
            type: boolean
            Indicates whether authentication should be used when connecting to the streaming server.
       *settings.username*
            type: String
            The username to use when accessing the streaming server. Only present if `use_auth` is `true`.
       *settings.password*
            type: String
            The password to use when accessing the streaming server. Only present if `use_auth` is `true`.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetStreamSettings'
        self.datain['type'] = None
        self.datain['settings'] = None

    def getType(self):
        return self.datain['type']

    def getSettings(self):
        return self.datain['settings']


class SaveStreamSettings(Baserequests):
    """Save the current streaming server settings to disk.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'SaveStreamSettings'


class SendCaptions(Baserequests):
    """Send the provided text as embedded CEA-608 caption data.

    :Arguments:
       *text*
            type: String
            Captions text
    """

    def __init__(self, text):
        Baserequests.__init__(self)
        self.name = 'SendCaptions'
        self.dataout['text'] = text


class GetStudioModeStatus(Baserequests):
    """Indicates if Studio Mode is currently enabled.

    :Returns:
       *studio_mode*
            type: boolean
            Indicates if Studio Mode is enabled.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetStudioModeStatus'
        self.datain['studio-mode'] = None

    def getStudioMode(self):
        return self.datain['studio-mode']


class GetPreviewScene(Baserequests):
    """Get the name of the currently previewed scene and its list of sources.
Will return an `error` if Studio Mode is not enabled.

    :Returns:
       *name*
            type: String
            The name of the active preview scene.
       *sources*
            type: Array<SceneItem>
            
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetPreviewScene'
        self.datain['sources'] = None
        self.datain['name'] = None

    def getSources(self):
        return self.datain['sources']

    def getName(self):
        return self.datain['name']


class SetPreviewScene(Baserequests):
    """Set the active preview scene.
Will return an `error` if Studio Mode is not enabled.

    :Arguments:
       *scene_name*
            type: String
            The name of the scene to preview.
    """

    def __init__(self, scene_name):
        Baserequests.__init__(self)
        self.name = 'SetPreviewScene'
        self.dataout['scene-name'] = scene_name


class TransitionToProgram(Baserequests):
    """Transitions the currently previewed scene to the main output.
Will return an `error` if Studio Mode is not enabled.

    :Arguments:
       *with_transition*
            type: Object (optional)
            Change the active transition before switching scenes. Defaults to the active transition.
       *with_transition.name*
            type: String
            Name of the transition.
       *with_transition.duration*
            type: int (optional)
            Transition duration (in milliseconds).
    """

    def __init__(self, with_transition):
        Baserequests.__init__(self)
        self.name = 'TransitionToProgram'
        self.dataout['with-transition'] = with_transition


class EnableStudioMode(Baserequests):
    """Enables Studio Mode.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'EnableStudioMode'


class DisableStudioMode(Baserequests):
    """Disables Studio Mode.

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'DisableStudioMode'


class ToggleStudioMode(Baserequests):
    """Toggles Studio Mode (depending on the current state of studio mode).

    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'ToggleStudioMode'


class GetTransitionList(Baserequests):
    """List of all transitions available in the frontend's dropdown menu.

    :Returns:
       *current_transition*
            type: String
            Name of the currently active transition.
       *transitions*
            type: Array<Object>
            List of transitions.
       *transitions.*.name*
            type: String
            Name of the transition.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetTransitionList'
        self.datain['transitions'] = None
        self.datain['current-transition'] = None

    def getTransitions(self):
        return self.datain['transitions']

    def getCurrentTransition(self):
        return self.datain['current-transition']


class GetCurrentTransition(Baserequests):
    """Get the name of the currently selected transition in the frontend's dropdown menu.

    :Returns:
       *name*
            type: String
            Name of the selected transition.
       *duration*
            type: int (optional)
            Transition duration (in milliseconds) if supported by the transition.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetCurrentTransition'
        self.datain['duration'] = None
        self.datain['name'] = None

    def getDuration(self):
        return self.datain['duration']

    def getName(self):
        return self.datain['name']


class SetCurrentTransition(Baserequests):
    """Set the active transition.

    :Arguments:
       *transition_name*
            type: String
            The name of the transition.
    """

    def __init__(self, transition_name):
        Baserequests.__init__(self)
        self.name = 'SetCurrentTransition'
        self.dataout['transition-name'] = transition_name


class SetTransitionDuration(Baserequests):
    """Set the duration of the currently selected transition if supported.

    :Arguments:
       *duration*
            type: int
            Desired duration of the transition (in milliseconds).
    """

    def __init__(self, duration):
        Baserequests.__init__(self)
        self.name = 'SetTransitionDuration'
        self.dataout['duration'] = duration


class GetTransitionDuration(Baserequests):
    """Get the duration of the currently selected transition if supported.

    :Returns:
       *transition_duration*
            type: int
            Duration of the current transition (in milliseconds).
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetTransitionDuration'
        self.datain['transition-duration'] = None

    def getTransitionDuration(self):
        return self.datain['transition-duration']


class GetTransitionPosition(Baserequests):
    """Get the position of the current transition.

    :Returns:
       *position*
            type: double
            current transition position. This value will be between 0.0 and 1.0. Note: Transition returns 1.0 when not active.
    """

    def __init__(self):
        Baserequests.__init__(self)
        self.name = 'GetTransitionPosition'
        self.datain['position'] = None

    def getPosition(self):
        return self.datain['position']


