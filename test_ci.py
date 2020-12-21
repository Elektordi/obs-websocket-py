import os
from obswebsocket import obsws, requests, events, cli

host = "127.0.0.1"
port = 4444
password = "secret"


def test_load():
    _ = obsws(host, port, password)
    # Just test everything is ok with the object...


def test_build_ok_requests():
    r = requests.GetVersion()
    assert r.name == "GetVersion"


def test_build_ok_events():
    e = events.Heartbeat()
    assert e.name == "Heartbeat"


def test_cli_parser():
    os.environ["OBS_WEBSOCKET_PASS"] = "obs-password"
    parser = cli.setup_parser()
    assert parser
    subparsers = parser._get_positional_actions()[0]
    # We expect at least these subcommands. Ideally would be kept up
    # to date so we remove commands
    expected_subcommands = {
        "PlayPauseMedia",
        "RestartMedia",
        "StopMedia",
        "NextMedia",
        "PreviousMedia",
        "GetMediaDuration",
        "GetMediaTime",
        "SetMediaTime",
        "ScrubMedia",
        "GetMediaState",
        "GetStreamingStatus",
        "StartStopStreaming",
        "StartStreaming",
        "StopStreaming",
        "SetStreamSettings",
        "GetStreamSettings",
        "SaveStreamSettings",
        "SendCaptions",
        "GetStudioModeStatus",
        "GetPreviewScene",
        "SetPreviewScene",
        "TransitionToProgram",
        "EnableStudioMode",
        "DisableStudioMode",
        "ToggleStudioMode",
        "ListOutputs",
        "GetOutputInfo",
        "StartOutput",
        "StopOutput",
        "GetReplayBufferStatus",
        "StartStopReplayBuffer",
        "StartReplayBuffer",
        "StopReplayBuffer",
        "SaveReplayBuffer",
        "SetCurrentScene",
        "GetCurrentScene",
        "GetSceneList",
        "CreateScene",
        "ReorderSceneItems",
        "SetSceneTransitionOverride",
        "RemoveSceneTransitionOverride",
        "GetSceneTransitionOverride",
        "SetCurrentProfile",
        "GetCurrentProfile",
        "ListProfiles",
        "GetVersion",
        "GetAuthRequired",
        "Authenticate",
        "SetHeartbeat",
        "SetFilenameFormatting",
        "GetFilenameFormatting",
        "GetStats",
        "BroadcastCustomMessage",
        "GetVideoInfo",
        "OpenProjector",
        "TriggerHotkeyByName",
        "TriggerHotkeyBySequence",
        "GetRecordingStatus",
        "StartStopRecording",
        "StartRecording",
        "StopRecording",
        "PauseRecording",
        "ResumeRecording",
        "SetRecordingFolder",
        "GetRecordingFolder",
        "GetMediaSourcesList",
        "CreateSource",
        "GetSourcesList",
        "GetSourceTypesList",
        "GetVolume",
        "SetVolume",
        "GetMute",
        "SetMute",
        "ToggleMute",
        "GetAudioActive",
        "SetSourceName",
        "SetSyncOffset",
        "GetSyncOffset",
        "GetSourceSettings",
        "SetSourceSettings",
        "GetTextGDIPlusProperties",
        "SetTextGDIPlusProperties",
        "GetTextFreetype2Properties",
        "SetTextFreetype2Properties",
        "GetBrowserSourceProperties",
        "SetBrowserSourceProperties",
        "GetSpecialSources",
        "GetSourceFilters",
        "GetSourceFilterInfo",
        "AddFilterToSource",
        "RemoveFilterFromSource",
        "ReorderSourceFilter",
        "MoveSourceFilter",
        "SetSourceFilterSettings",
        "SetSourceFilterVisibility",
        "GetAudioMonitorType",
        "SetAudioMonitorType",
        "TakeSourceScreenshot",
        "SetCurrentSceneCollection",
        "GetCurrentSceneCollection",
        "ListSceneCollections",
        "GetTransitionList",
        "GetCurrentTransition",
        "SetCurrentTransition",
        "SetTransitionDuration",
        "GetTransitionDuration",
        "GetTransitionPosition",
        "GetTransitionSettings",
        "SetTransitionSettings",
        "ReleaseTBar",
        "SetTBarPosition",
        "GetSceneItemList",
        "GetSceneItemProperties",
        "SetSceneItemProperties",
        "ResetSceneItem",
        "SetSceneItemRender",
        "SetSceneItemPosition",
        "SetSceneItemTransform",
        "SetSceneItemCrop",
        "DeleteSceneItem",
        "AddSceneItem",
        "DuplicateSceneItem",
    }
    assert not expected_subcommands - set(subparsers.choices.keys())

    # Basic arguments + environ parsing
    args = parser.parse_args(["--host", "hostname", "--port", "1234", "GetVideoInfo"])
    assert args.host == "hostname"
    assert args.port == 1234
    assert args.password == "obs-password"
    assert args.command == "GetVideoInfo"

    # More complex command parsing
    args = parser.parse_args(
        ["SetSourceSettings", "SourceName", 'json:{"looping": true}', "ffmpeg_source"]
    )
    assert args.command == "SetSourceSettings"
    # These will change depending on the sub-command
    assert args.sourceName == "SourceName"
    assert args.sourceSettings == 'json:{"looping": true}'
    assert args.sourceType == "ffmpeg_source"
