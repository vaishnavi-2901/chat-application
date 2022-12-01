from datetime import datetime
from tkinter.messagebox import NO
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    print(request)
    return render(request, 'chat/room.html', {
        'room_name':room_name
    })

def login(request):
    print("sdsds")
    return render(request, 'chat/room.html')
