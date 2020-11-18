#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (Generated on 2020-11-18 11:01:42.391928) #

from .base_classes import Baseevents


class SwitchScenes(Baseevents):
    """Indicates a scene change.

    :Returns:
       *scene_name*
            type: String
            The new scene.
       *sources*
            type: Array<SceneItem>
            List of scene items in the new scene. Same specification as [`GetCurrentScene`](#getcurrentscene).
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SwitchScenes'
        self.datain['sources'] = None
        self.datain['scene-name'] = None

    def getSources(self):
        return self.datain['sources']

    def getSceneName(self):
        return self.datain['scene-name']


class ScenesChanged(Baseevents):
    """

Note: This event is not fired when the scenes are reordered.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ScenesChanged'


class SceneCollectionChanged(Baseevents):
    """Triggered when switching to another scene collection or when renaming the current scene collection.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneCollectionChanged'


class SceneCollectionListChanged(Baseevents):
    """Triggered when a scene collection is created, added, renamed, or removed.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneCollectionListChanged'


class SwitchTransition(Baseevents):
    """The active transition has been changed.

    :Returns:
       *transition_name*
            type: String
            The name of the new active transition.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SwitchTransition'
        self.datain['transition-name'] = None

    def getTransitionName(self):
        return self.datain['transition-name']


class TransitionListChanged(Baseevents):
    """The list of available transitions has been modified.
Transitions have been added, removed, or renamed.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'TransitionListChanged'


class TransitionDurationChanged(Baseevents):
    """The active transition duration has been changed.

    :Returns:
       *new_duration*
            type: int
            New transition duration.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'TransitionDurationChanged'
        self.datain['new-duration'] = None

    def getNewDuration(self):
        return self.datain['new-duration']


class TransitionBegin(Baseevents):
    """A transition (other than "cut") has begun.

    :Returns:
       *name*
            type: String
            Transition name.
       *type*
            type: String
            Transition type.
       *duration*
            type: int
            Transition duration (in milliseconds). Will be -1 for any transition with a fixed duration, such as a Stinger, due to limitations of the OBS API.
       *from_scene*
            type: String
            Source scene of the transition
       *to_scene*
            type: String
            Destination scene of the transition
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'TransitionBegin'
        self.datain['from-scene'] = None
        self.datain['to-scene'] = None
        self.datain['duration'] = None
        self.datain['type'] = None
        self.datain['name'] = None

    def getFromScene(self):
        return self.datain['from-scene']

    def getToScene(self):
        return self.datain['to-scene']

    def getDuration(self):
        return self.datain['duration']

    def getType(self):
        return self.datain['type']

    def getName(self):
        return self.datain['name']


class TransitionEnd(Baseevents):
    """A transition (other than "cut") has ended.
Please note that the `from-scene` field is not available in TransitionEnd.

    :Returns:
       *name*
            type: String
            Transition name.
       *type*
            type: String
            Transition type.
       *duration*
            type: int
            Transition duration (in milliseconds).
       *to_scene*
            type: String
            Destination scene of the transition
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'TransitionEnd'
        self.datain['duration'] = None
        self.datain['name'] = None
        self.datain['to-scene'] = None
        self.datain['type'] = None

    def getDuration(self):
        return self.datain['duration']

    def getName(self):
        return self.datain['name']

    def getToScene(self):
        return self.datain['to-scene']

    def getType(self):
        return self.datain['type']


class TransitionVideoEnd(Baseevents):
    """A stinger transition has finished playing its video.

    :Returns:
       *name*
            type: String
            Transition name.
       *type*
            type: String
            Transition type.
       *duration*
            type: int
            Transition duration (in milliseconds).
       *from_scene*
            type: String
            Source scene of the transition
       *to_scene*
            type: String
            Destination scene of the transition
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'TransitionVideoEnd'
        self.datain['from-scene'] = None
        self.datain['to-scene'] = None
        self.datain['duration'] = None
        self.datain['type'] = None
        self.datain['name'] = None

    def getFromScene(self):
        return self.datain['from-scene']

    def getToScene(self):
        return self.datain['to-scene']

    def getDuration(self):
        return self.datain['duration']

    def getType(self):
        return self.datain['type']

    def getName(self):
        return self.datain['name']


class ProfileChanged(Baseevents):
    """Triggered when switching to another profile or when renaming the current profile.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ProfileChanged'


class ProfileListChanged(Baseevents):
    """Triggered when a profile is created, added, renamed, or removed.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ProfileListChanged'


class StreamStarting(Baseevents):
    """A request to start streaming has been issued.

    :Returns:
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'StreamStarting'
        self.datain['preview-only'] = None

    def getPreviewOnly(self):
        return self.datain['preview-only']


class StreamStarted(Baseevents):
    """Streaming started successfully.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'StreamStarted'


class StreamStopping(Baseevents):
    """A request to stop streaming has been issued.

    :Returns:
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'StreamStopping'
        self.datain['preview-only'] = None

    def getPreviewOnly(self):
        return self.datain['preview-only']


class StreamStopped(Baseevents):
    """Streaming stopped successfully.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'StreamStopped'


class StreamStatus(Baseevents):
    """Emitted every 2 seconds when stream is active.

    :Returns:
       *streaming*
            type: boolean
            Current streaming state.
       *recording*
            type: boolean
            Current recording state.
       *replay_buffer_active*
            type: boolean
            Replay Buffer status
       *bytes_per_sec*
            type: int
            Amount of data per second (in bytes) transmitted by the stream encoder.
       *kbits_per_sec*
            type: int
            Amount of data per second (in kilobits) transmitted by the stream encoder.
       *strain*
            type: double
            Percentage of dropped frames.
       *total_stream_time*
            type: int
            Total time (in seconds) since the stream started.
       *num_total_frames*
            type: int
            Total number of frames transmitted since the stream started.
       *num_dropped_frames*
            type: int
            Number of frames dropped by the encoder since the stream started.
       *fps*
            type: double
            Current framerate.
       *render_total_frames*
            type: int
            Number of frames rendered
       *render_missed_frames*
            type: int
            Number of frames missed due to rendering lag
       *output_total_frames*
            type: int
            Number of frames outputted
       *output_skipped_frames*
            type: int
            Number of frames skipped due to encoding lag
       *average_frame_time*
            type: double
            Average frame time (in milliseconds)
       *cpu_usage*
            type: double
            Current CPU usage (percentage)
       *memory_usage*
            type: double
            Current RAM usage (in megabytes)
       *free_disk_space*
            type: double
            Free recording disk space (in megabytes)
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'StreamStatus'
        self.datain['replay-buffer-active'] = None
        self.datain['streaming'] = None
        self.datain['kbits-per-sec'] = None
        self.datain['output-skipped-frames'] = None
        self.datain['bytes-per-sec'] = None
        self.datain['output-total-frames'] = None
        self.datain['num-total-frames'] = None
        self.datain['total-stream-time'] = None
        self.datain['strain'] = None
        self.datain['fps'] = None
        self.datain['render-total-frames'] = None
        self.datain['num-dropped-frames'] = None
        self.datain['render-missed-frames'] = None
        self.datain['preview-only'] = None
        self.datain['average-frame-time'] = None
        self.datain['free-disk-space'] = None
        self.datain['recording'] = None
        self.datain['cpu-usage'] = None
        self.datain['memory-usage'] = None

    def getReplayBufferActive(self):
        return self.datain['replay-buffer-active']

    def getStreaming(self):
        return self.datain['streaming']

    def getKbitsPerSec(self):
        return self.datain['kbits-per-sec']

    def getOutputSkippedFrames(self):
        return self.datain['output-skipped-frames']

    def getBytesPerSec(self):
        return self.datain['bytes-per-sec']

    def getOutputTotalFrames(self):
        return self.datain['output-total-frames']

    def getNumTotalFrames(self):
        return self.datain['num-total-frames']

    def getTotalStreamTime(self):
        return self.datain['total-stream-time']

    def getStrain(self):
        return self.datain['strain']

    def getFps(self):
        return self.datain['fps']

    def getRenderTotalFrames(self):
        return self.datain['render-total-frames']

    def getNumDroppedFrames(self):
        return self.datain['num-dropped-frames']

    def getRenderMissedFrames(self):
        return self.datain['render-missed-frames']

    def getPreviewOnly(self):
        return self.datain['preview-only']

    def getAverageFrameTime(self):
        return self.datain['average-frame-time']

    def getFreeDiskSpace(self):
        return self.datain['free-disk-space']

    def getRecording(self):
        return self.datain['recording']

    def getCpuUsage(self):
        return self.datain['cpu-usage']

    def getMemoryUsage(self):
        return self.datain['memory-usage']


class RecordingStarting(Baseevents):
    """A request to start recording has been issued.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'RecordingStarting'


class RecordingStarted(Baseevents):
    """Recording started successfully.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'RecordingStarted'


class RecordingStopping(Baseevents):
    """A request to stop recording has been issued.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'RecordingStopping'


class RecordingStopped(Baseevents):
    """Recording stopped successfully.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'RecordingStopped'


class RecordingPaused(Baseevents):
    """Current recording paused

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'RecordingPaused'


class RecordingResumed(Baseevents):
    """Current recording resumed

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'RecordingResumed'


class ReplayStarting(Baseevents):
    """A request to start the replay buffer has been issued.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ReplayStarting'


class ReplayStarted(Baseevents):
    """Replay Buffer started successfully

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ReplayStarted'


class ReplayStopping(Baseevents):
    """A request to stop the replay buffer has been issued.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ReplayStopping'


class ReplayStopped(Baseevents):
    """Replay Buffer stopped successfully

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'ReplayStopped'


class Exiting(Baseevents):
    """OBS is exiting.

    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'Exiting'


class Heartbeat(Baseevents):
    """Emitted every 2 seconds after enabling it by calling SetHeartbeat.

    :Returns:
       *pulse*
            type: boolean
            Toggles between every JSON message as an "I am alive" indicator.
       *current_profile*
            type: string (optional)
            Current active profile.
       *current_scene*
            type: string (optional)
            Current active scene.
       *streaming*
            type: boolean (optional)
            Current streaming state.
       *total_stream_time*
            type: int (optional)
            Total time (in seconds) since the stream started.
       *total_stream_bytes*
            type: int (optional)
            Total bytes sent since the stream started.
       *total_stream_frames*
            type: int (optional)
            Total frames streamed since the stream started.
       *recording*
            type: boolean (optional)
            Current recording state.
       *total_record_time*
            type: int (optional)
            Total time (in seconds) since recording started.
       *total_record_bytes*
            type: int (optional)
            Total bytes recorded since the recording started.
       *total_record_frames*
            type: int (optional)
            Total frames recorded since the recording started.
       *stats*
            type: OBSStats
            OBS Stats
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'Heartbeat'
        self.datain['total-stream-time'] = None
        self.datain['total-stream-bytes'] = None
        self.datain['total-record-frames'] = None
        self.datain['pulse'] = None
        self.datain['total-stream-frames'] = None
        self.datain['streaming'] = None
        self.datain['stats'] = None
        self.datain['recording'] = None
        self.datain['current-scene'] = None
        self.datain['total-record-time'] = None
        self.datain['total-record-bytes'] = None
        self.datain['current-profile'] = None

    def getTotalStreamTime(self):
        return self.datain['total-stream-time']

    def getTotalStreamBytes(self):
        return self.datain['total-stream-bytes']

    def getTotalRecordFrames(self):
        return self.datain['total-record-frames']

    def getPulse(self):
        return self.datain['pulse']

    def getTotalStreamFrames(self):
        return self.datain['total-stream-frames']

    def getStreaming(self):
        return self.datain['streaming']

    def getStats(self):
        return self.datain['stats']

    def getRecording(self):
        return self.datain['recording']

    def getCurrentScene(self):
        return self.datain['current-scene']

    def getTotalRecordTime(self):
        return self.datain['total-record-time']

    def getTotalRecordBytes(self):
        return self.datain['total-record-bytes']

    def getCurrentProfile(self):
        return self.datain['current-profile']


class BroadcastCustomMessage(Baseevents):
    """A custom broadcast message, sent by the server, requested by one of the websocket clients.

    :Returns:
       *realm*
            type: String
            Identifier provided by the sender
       *data*
            type: Object
            User-defined data
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'BroadcastCustomMessage'
        self.datain['data'] = None
        self.datain['realm'] = None

    def getData(self):
        return self.datain['data']

    def getRealm(self):
        return self.datain['realm']


class SourceCreated(Baseevents):
    """A source has been created. A source can be an input, a scene or a transition.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceType*
            type: String
            Source type. Can be "input", "scene", "transition" or "filter".
       *sourceKind*
            type: String
            Source kind.
       *sourceSettings*
            type: Object
            Source settings
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceCreated'
        self.datain['sourceKind'] = None
        self.datain['sourceSettings'] = None
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcesettings(self):
        return self.datain['sourceSettings']

    def getSourcename(self):
        return self.datain['sourceName']

    def getSourcetype(self):
        return self.datain['sourceType']


class SourceDestroyed(Baseevents):
    """A source has been destroyed/removed. A source can be an input, a scene or a transition.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceType*
            type: String
            Source type. Can be "input", "scene", "transition" or "filter".
       *sourceKind*
            type: String
            Source kind.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceDestroyed'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']

    def getSourcetype(self):
        return self.datain['sourceType']


class SourceVolumeChanged(Baseevents):
    """The volume of a source has changed.

    :Returns:
       *sourceName*
            type: String
            Source name
       *volume*
            type: float
            Source volume
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceVolumeChanged'
        self.datain['volume'] = None
        self.datain['sourceName'] = None

    def getVolume(self):
        return self.datain['volume']

    def getSourcename(self):
        return self.datain['sourceName']


class SourceMuteStateChanged(Baseevents):
    """A source has been muted or unmuted.

    :Returns:
       *sourceName*
            type: String
            Source name
       *muted*
            type: boolean
            Mute status of the source
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceMuteStateChanged'
        self.datain['muted'] = None
        self.datain['sourceName'] = None

    def getMuted(self):
        return self.datain['muted']

    def getSourcename(self):
        return self.datain['sourceName']


class SourceAudioDeactivated(Baseevents):
    """A source has removed audio.

    :Returns:
       *sourceName*
            type: String
            Source name
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceAudioDeactivated'
        self.datain['sourceName'] = None

    def getSourcename(self):
        return self.datain['sourceName']


class SourceAudioActivated(Baseevents):
    """A source has added audio.

    :Returns:
       *sourceName*
            type: String
            Source name
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceAudioActivated'
        self.datain['sourceName'] = None

    def getSourcename(self):
        return self.datain['sourceName']


class SourceAudioSyncOffsetChanged(Baseevents):
    """The audio sync offset of a source has changed.

    :Returns:
       *sourceName*
            type: String
            Source name
       *syncOffset*
            type: int
            Audio sync offset of the source (in nanoseconds)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceAudioSyncOffsetChanged'
        self.datain['syncOffset'] = None
        self.datain['sourceName'] = None

    def getSyncoffset(self):
        return self.datain['syncOffset']

    def getSourcename(self):
        return self.datain['sourceName']


class SourceAudioMixersChanged(Baseevents):
    """Audio mixer routing changed on a source.

    :Returns:
       *sourceName*
            type: String
            Source name
       *mixers*
            type: Array<Object>
            Routing status of the source for each audio mixer (array of 6 values)
       *mixers.*.id*
            type: int
            Mixer number
       *mixers.*.enabled*
            type: boolean
            Routing status
       *hexMixersValue*
            type: String
            Raw mixer flags (little-endian, one bit per mixer) as an hexadecimal value
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceAudioMixersChanged'
        self.datain['hexMixersValue'] = None
        self.datain['mixers'] = None
        self.datain['sourceName'] = None

    def getHexmixersvalue(self):
        return self.datain['hexMixersValue']

    def getMixers(self):
        return self.datain['mixers']

    def getSourcename(self):
        return self.datain['sourceName']


class SourceRenamed(Baseevents):
    """A source has been renamed.

    :Returns:
       *previousName*
            type: String
            Previous source name
       *newName*
            type: String
            New source name
       *sourceType*
            type: String
            Type of source (input, scene, filter, transition)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceRenamed'
        self.datain['newName'] = None
        self.datain['previousName'] = None
        self.datain['sourceType'] = None

    def getNewname(self):
        return self.datain['newName']

    def getPreviousname(self):
        return self.datain['previousName']

    def getSourcetype(self):
        return self.datain['sourceType']


class SourceFilterAdded(Baseevents):
    """A filter was added to a source.

    :Returns:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Filter name
       *filterType*
            type: String
            Filter type
       *filterSettings*
            type: Object
            Filter settings
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceFilterAdded'
        self.datain['filterName'] = None
        self.datain['filterSettings'] = None
        self.datain['sourceName'] = None
        self.datain['filterType'] = None

    def getFiltername(self):
        return self.datain['filterName']

    def getFiltersettings(self):
        return self.datain['filterSettings']

    def getSourcename(self):
        return self.datain['sourceName']

    def getFiltertype(self):
        return self.datain['filterType']


class SourceFilterRemoved(Baseevents):
    """A filter was removed from a source.

    :Returns:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Filter name
       *filterType*
            type: String
            Filter type
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceFilterRemoved'
        self.datain['filterName'] = None
        self.datain['sourceName'] = None
        self.datain['filterType'] = None

    def getFiltername(self):
        return self.datain['filterName']

    def getSourcename(self):
        return self.datain['sourceName']

    def getFiltertype(self):
        return self.datain['filterType']


class SourceFilterVisibilityChanged(Baseevents):
    """The visibility/enabled state of a filter changed

    :Returns:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Filter name
       *filterEnabled*
            type: Boolean
            New filter state
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceFilterVisibilityChanged'
        self.datain['filterName'] = None
        self.datain['filterEnabled'] = None
        self.datain['sourceName'] = None

    def getFiltername(self):
        return self.datain['filterName']

    def getFilterenabled(self):
        return self.datain['filterEnabled']

    def getSourcename(self):
        return self.datain['sourceName']


class SourceFiltersReordered(Baseevents):
    """Filters in a source have been reordered.

    :Returns:
       *sourceName*
            type: String
            Source name
       *filters*
            type: Array<Object>
            Ordered Filters list
       *filters.*.name*
            type: String
            Filter name
       *filters.*.type*
            type: String
            Filter type
       *filters.*.enabled*
            type: boolean
            Filter visibility status
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceFiltersReordered'
        self.datain['filters'] = None
        self.datain['sourceName'] = None

    def getFilters(self):
        return self.datain['filters']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaPlaying(Baseevents):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaPlaying'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaPaused(Baseevents):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaPaused'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaRestarted(Baseevents):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaRestarted'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaStopped(Baseevents):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaStopped'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaNext(Baseevents):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaNext'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaPrevious(Baseevents):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaPrevious'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaStarted(Baseevents):
    """

Note: These events are emitted by the OBS sources themselves. For example when the media file starts playing. The behavior depends on the type of media source being used.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaStarted'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class MediaEnded(Baseevents):
    """

Note: These events are emitted by the OBS sources themselves. For example when the media file ends. The behavior depends on the type of media source being used.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'MediaEnded'
        self.datain['sourceKind'] = None
        self.datain['sourceName'] = None

    def getSourcekind(self):
        return self.datain['sourceKind']

    def getSourcename(self):
        return self.datain['sourceName']


class SourceOrderChanged(Baseevents):
    """Scene items within a scene have been reordered.

    :Returns:
       *scene_name*
            type: String
            Name of the scene where items have been reordered.
       *scene_items*
            type: Array<Object>
            Ordered list of scene items
       *scene_items.*.source_name*
            type: String
            Item source name
       *scene_items.*.item_id*
            type: int
            Scene item unique ID
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SourceOrderChanged'
        self.datain['scene-items'] = None
        self.datain['scene-name'] = None

    def getSceneItems(self):
        return self.datain['scene-items']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemAdded(Baseevents):
    """A scene item has been added to a scene.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item added to the scene.
       *item_id*
            type: int
            Scene item ID
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemAdded'
        self.datain['item-id'] = None
        self.datain['item-name'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemName(self):
        return self.datain['item-name']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemRemoved(Baseevents):
    """A scene item has been removed from a scene.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item removed from the scene.
       *item_id*
            type: int
            Scene item ID
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemRemoved'
        self.datain['item-id'] = None
        self.datain['item-name'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemName(self):
        return self.datain['item-name']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemVisibilityChanged(Baseevents):
    """A scene item's visibility has been toggled.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *item_visible*
            type: boolean
            New visibility state of the item.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemVisibilityChanged'
        self.datain['item-id'] = None
        self.datain['item-name'] = None
        self.datain['item-visible'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemName(self):
        return self.datain['item-name']

    def getItemVisible(self):
        return self.datain['item-visible']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemLockChanged(Baseevents):
    """A scene item's locked status has been toggled.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *item_locked*
            type: boolean
            New locked state of the item.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemLockChanged'
        self.datain['item-id'] = None
        self.datain['item-locked'] = None
        self.datain['item-name'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemLocked(self):
        return self.datain['item-locked']

    def getItemName(self):
        return self.datain['item-name']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemTransformChanged(Baseevents):
    """A scene item's transform has been changed.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *transform*
            type: SceneItemTransform
            Scene item transform properties
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemTransformChanged'
        self.datain['item-id'] = None
        self.datain['item-name'] = None
        self.datain['transform'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemName(self):
        return self.datain['item-name']

    def getTransform(self):
        return self.datain['transform']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemSelected(Baseevents):
    """A scene item is selected.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Name of the item in the scene.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemSelected'
        self.datain['item-id'] = None
        self.datain['item-name'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemName(self):
        return self.datain['item-name']

    def getSceneName(self):
        return self.datain['scene-name']


class SceneItemDeselected(Baseevents):
    """A scene item is deselected.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Name of the item in the scene.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'SceneItemDeselected'
        self.datain['item-id'] = None
        self.datain['item-name'] = None
        self.datain['scene-name'] = None

    def getItemId(self):
        return self.datain['item-id']

    def getItemName(self):
        return self.datain['item-name']

    def getSceneName(self):
        return self.datain['scene-name']


class PreviewSceneChanged(Baseevents):
    """The selected preview scene has changed (only available in Studio Mode).

    :Returns:
       *scene_name*
            type: String
            Name of the scene being previewed.
       *sources*
            type: Array<SceneItem>
            List of sources composing the scene. Same specification as [`GetCurrentScene`](#getcurrentscene).
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'PreviewSceneChanged'
        self.datain['sources'] = None
        self.datain['scene-name'] = None

    def getSources(self):
        return self.datain['sources']

    def getSceneName(self):
        return self.datain['scene-name']


class StudioModeSwitched(Baseevents):
    """Studio Mode has been enabled or disabled.

    :Returns:
       *new_state*
            type: boolean
            The new enabled state of Studio Mode.
    """

    def __init__(self):
        Baseevents.__init__(self)
        self.name = 'StudioModeSwitched'
        self.datain['new-state'] = None

    def getNewState(self):
        return self.datain['new-state']


