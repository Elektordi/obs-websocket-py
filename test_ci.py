from unittest.mock import patch, Mock
from queue import Queue, Empty
import time

from obswebsocket import obsws, requests, events


def fake_send(data):
    if data == '{"request-type": "GetAuthRequired", "message-id": "1"}':
        fake_recv.queue.put('{"status":"ok"}')
    elif data == '{"message-id": "2", "request-type": "FakeRequest"}':
        fake_recv.queue.put('{"message-id": "2", "status":"ok"}')
    elif data == '{"op": 1, "d": {"rpcVersion": 1, "authentication": "", "eventSubscriptions": 1023}}':
        fake_recv.queue.put('{"op": 2, "d": {"negotiatedRpcVersion": 1 }}')
    elif data == '{"op": 6, "d": {"requestId": "1", "requestType": "FakeRequest", "requestData": {}}}':
        fake_recv.queue.put('{"op": 7, "d": {"requestId": "1", "requestType": "FakeRequest", "requestStatus": {"result": true, "code": 100}}}')
    else:
        raise Exception(data)


def fake_recv():
    try:
        return fake_recv.queue.get(timeout=1)
    except Empty:
        return ""
fake_recv.queue = Queue()   # noqa: E305


def test_request_legacy():
    ws = obsws("127.0.0.1", 4444, "", legacy=True)
    with patch('websocket.WebSocket') as mock:
        mockws = mock.return_value
        mockws.send = Mock(wraps=fake_send)
        mockws.recv = Mock(wraps=fake_recv)

        ws.connect()
        mockws.connect.assert_called_once_with("ws://127.0.0.1:4444")
        assert ws.thread_recv.running

        r = ws.call(requests.FakeRequest())
        assert r.name == "FakeRequest"
        assert r.status

        ws.disconnect()
        assert not ws.thread_recv


def test_event_legacy():
    ws = obsws("127.0.0.1", 4444, "", legacy=True)
    with patch('websocket.WebSocket') as mock:
        mockws = mock.return_value
        mockws.send = Mock(wraps=fake_send)
        mockws.recv = Mock(wraps=fake_recv)

        ws.connect()
        mockws.connect.assert_called_once_with("ws://127.0.0.1:4444")
        assert ws.thread_recv.running

        def on_fake_event(message):
            assert message.name == "FakeEvent"
            assert message.getFakeKey() == "fakeValue"
            on_fake_event.ok = True

        on_fake_event.ok = False
        ws.register(on_fake_event, events.FakeEvent)
        fake_recv.queue.put('{"update-type": "FakeEvent", "fakeKey":"fakeValue"}')
        time.sleep(1)
        assert on_fake_event.ok

        ws.disconnect()
        assert not ws.thread_recv


def test_request():
    ws = obsws("127.0.0.1", 4455, "")
    with patch('websocket.WebSocket') as mock:
        mockws = mock.return_value
        mockws.send = Mock(wraps=fake_send)
        mockws.recv = Mock(wraps=fake_recv)

        fake_recv.queue.put('{"op": 0, "d": { "obsWebSocketVersion": "fake", "rpcVersion": 1 }}')
        ws.connect()
        mockws.connect.assert_called_once_with("ws://127.0.0.1:4455")
        assert ws.thread_recv.running

        r = ws.call(requests.FakeRequest())
        assert r.name == "FakeRequest"
        assert r.status

        ws.disconnect()
        assert not ws.thread_recv


def test_event():
    ws = obsws("127.0.0.1", 4455, "")
    with patch('websocket.WebSocket') as mock:
        mockws = mock.return_value
        mockws.send = Mock(wraps=fake_send)
        mockws.recv = Mock(wraps=fake_recv)

        fake_recv.queue.put('{"op": 0, "d": { "obsWebSocketVersion": "fake", "rpcVersion": 1 }}')
        ws.connect()
        mockws.connect.assert_called_once_with("ws://127.0.0.1:4455")
        assert ws.thread_recv.running

        def on_fake_event(message):
            assert message.name == "FakeEvent"
            assert message.getFakeKey() == "fakeValue"
            on_fake_event.ok = True

        on_fake_event.ok = False
        ws.register(on_fake_event, events.FakeEvent)
        fake_recv.queue.put('{"op": 5, "d": { "eventType": "FakeEvent", "eventIntent": 1, "eventData": { "fakeKey": "fakeValue" }}}')
        time.sleep(1)
        assert on_fake_event.ok

        ws.disconnect()
        assert not ws.thread_recv
