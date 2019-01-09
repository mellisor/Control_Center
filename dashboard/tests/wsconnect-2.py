# Requires websocket-client
import websocket
import time
from threading import Thread
import json

id = 'IFLTWXG26YQVA6289X22'
key = '12d530d6-db89-45a3-a616-b8ad6c72ea74'
join_msg = {
    'id' : id,
    'key' : key,
    'command' : 'join',
}

def on_message(ws, message):
    print(message)

def on_error(ws,error):
    print(error)

def on_close(ws):
    print("Closed")

def on_open(ws):
    ws.send(json.dumps(join_msg))
    msg = {
        'command' : 'message',
        'project' : 'IFLTWXG26YQVA6289X22',
        'name' : 'speed',
        'value' : 5
    }
    ws.send(json.dumps(msg))
        
        
if __name__ == '__main__':
    ws = websocket.WebSocketApp("ws://localhost:8000/comm/stream/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
