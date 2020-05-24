Logs when ran the frontend server which opens a websocket connection to ws://127.0.0.1:8000/api/  :


```WebSocket HANDSHAKING /api/ [127.0.0.1:50650]
ws connected {'type': 'websocket.connect'}
HTTP GET /api/ 200 [0.01, 127.0.0.1:50660]
WebSocket DISCONNECT /api/ [127.0.0.1:50650]
ws disconnected {'type': 'websocket.disconnect', 'code': 1006}
WebSocket HANDSHAKING /api/ [127.0.0.1:50698]
ws connected {'type': 'websocket.connect'}
WebSocket DISCONNECT /api/ [127.0.0.1:50698]
ws disconnected {'type': 'websocket.disconnect', 'code': 1006}
WebSocket HANDSHAKING /api/ [127.0.0.1:50740]
ws connected {'type': 'websocket.connect'}
WebSocket DISCONNECT /api/ [127.0.0.1:50740]
ws disconnected {'type': 'websocket.disconnect', 'code': 1006}
WebSocket HANDSHAKING /api/ [127.0.0.1:50782]
ws connected {'type': 'websocket.connect'}
Application instance <Task pending coro=<AsyncConsumer.__call__() running at /home/prateek/Misc/Programming/WebDev/MaterialUIProject/backend/env/lib/python3.6/site-packages/channels/consumer.py:62> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7fcb6ab740d8>()]>> for connection <WebSocketProtocol client=['127.0.0.1', 50650] path=b'/api/'> took too long to shut down and was killed.
WebSocket DISCONNECT /api/ [127.0.0.1:50782]
ws disconnected {'type': 'websocket.disconnect', 'code': 1006}
Application instance <Task pending coro=<AsyncConsumer.__call__() running at /home/prateek/Misc/Programming/WebDev/MaterialUIProject/backend/env/lib/python3.6/site-packages/channels/consumer.py:62> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7fcb6aa94408>()]>> for connection <WebSocketProtocol client=['127.0.0.1', 50698] path=b'/api/'> took too long to shut down and was killed.
Application instance <Task pending coro=<AsyncConsumer.__call__() running at /home/prateek/Misc/Programming/WebDev/MaterialUIProject/backend/env/lib/python3.6/site-packages/channels/consumer.py:62> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7fcb6a987bb8>()]>> for connection <WebSocketProtocol client=['127.0.0.1', 50740] path=b'/api/'> took too long to shut down and was killed.```

