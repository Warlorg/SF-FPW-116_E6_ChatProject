import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import generics

from .models import Room, Message
from .serializers import RoomSerializer


@login_required
def rooms(request):
    rooms = Room.objects.all().values()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room, created = Room.objects.get_or_create(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    # Get all users in the room
    room_users = room.users.all()
    logging.debug(f'room_users: {room_users}')

    return render(request, 'room/room.html',
                  {'room': room, 'messages': messages, 'room_users': room_users})


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
