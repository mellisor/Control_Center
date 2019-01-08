import asyncio
import websockets
import json

async def hello():
    async with websockets.connect('ws://localhost:8000/comm/stream/') as w:
        msg = {'hi': 'pal'}
        await w.send(json.dumps(msg))
        resp = await w.recv()
        print(f"< {resp}")

asyncio.get_event_loop().run_until_complete(hello())