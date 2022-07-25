import asyncio
import websockets
from .models import History
import django


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message)
        spli = str(message).split('-')
        x = History()
        x.user_id = spli[0]
        x.url = spli[1]
        x.save()


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


django.setup()
asyncio.run(main())