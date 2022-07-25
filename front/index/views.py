import asyncio
import uuid

import websockets
from django.http import HttpResponse
from django.shortcuts import render


def send_info_server(func):
    def inner1(*args, **kwargs):
        end_user_id, ret_render = return_id(func(*args, **kwargs), args[0])
        send(args[0], end_user_id)
        return ret_render

    return inner1


async def hello(end_user_id, web_page_url):
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(f"{end_user_id},{web_page_url}")
        await websocket.recv()


def send(request, end_user_id):
    web_page_url = request.get_host() + request.path
    try:
        asyncio.run(hello(end_user_id, web_page_url))
    except:
        print('lose connection')


def return_id(ret_render, request):
    try:
        end_user_id = request.COOKIES['id']
    except:
        end_user_id = uuid.uuid1()
        ret_render.set_cookie('id', end_user_id, max_age=None)
    return end_user_id, ret_render


@send_info_server
def home(request):
    return render(request, 'index.html')


@send_info_server
def about(request):
    return render(request, 'about.html')


@send_info_server
def contact(request):
    return render(request, 'contact.html')


@send_info_server
def course_details(request):
    return render(request, 'course-details.html')


@send_info_server
def courses(request):
    return render(request, 'courses.html')


@send_info_server
def events(request):
    return render(request, 'events.html')


@send_info_server
def pricing(request):
    return render(request, 'pricing.html')


@send_info_server
def trainers(request):
    return render(request, 'trainers.html')
