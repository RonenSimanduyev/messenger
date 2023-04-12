from django.shortcuts import render


def index(request):
    return render(request, "messengerApp/index.html")


def room(request, room_name):
    return render(request, "messengerApp/room.html", {"room_name": room_name})