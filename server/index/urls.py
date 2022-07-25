








from django.contrib import admin
from django.urls import path, include
from . import views

from .models import History


urlpatterns = [
    path('', views.home)
]





def one_time_startup():
    asyncio.run(main())



import asyncio
import websockets
import threading
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
#
# task = threading.Thread(target=one_time_startup())#, args=(pair,)
# task.start()
# print('111')
#one_time_startup()
#asyncio.run(main())