import asyncio
import websockets
import json

async def hello():
    async with websockets.connect('ws://localhost:8000/comm/stream/') as w:
        msg = {
                'command': 'join',
                'id' : 'IFLTWXG26YQVA6289X22',
                'key' : '12d530d6-db89-45a3-a616-b8ad6c72ea74',
        }
        await w.send(json.dumps(msg))
        async for msg in w:
                print(msg)

asyncio.get_event_loop().run_until_complete(hello())
