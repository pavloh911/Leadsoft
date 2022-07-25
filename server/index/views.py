import threading

from django.shortcuts import render, HttpResponse
from .models import History
import threading
from asgiref.sync import sync_to_async
import asyncio
import websockets

# Create your views here.
thread_a = None

def home(request):
    global thread_a
    info = ''
    async def echo(websocket):
        async for message in websocket:
            await websocket.send(message)
            print(message)
            await save_message(message)


    @sync_to_async
    def save_message(message):
        spli = str(message).split(',')
        x = History()
        x.user_id = spli[0]
        x.url = spli[1]
        x.save()

    async def main():
        info = 'sever start'
        async with websockets.serve(echo, "localhost", 8765):
            await asyncio.Future()  # run forever

    def a():
        asyncio.run(main())


    if not thread_a:
        thread_a = threading.Thread(target=a)
    try:
        thread_a.start()
    except:
        info = 'server work'

    obj = History.objects.all()
    if request.method == 'POST':
        post_filter = request.POST['filter']
        if post_filter == 'all':
            history = obj.order_by('-date')
        else:
            history = obj.filter(user_id=post_filter)
    else:
        history = obj.order_by('-date')
    return render(request, 'index.html', {'history': history, 'info': info})
