from obswebsocket import obsws, requests, events

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
