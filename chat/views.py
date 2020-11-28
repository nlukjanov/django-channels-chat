from django.shortcuts import render


def index(request):
    """
    chat index view
    """
    return render(request, 'index.html', {})


def room(request, room_name):
    """
    chat room view
    """
    return render(request, 'chatroom.html', {
        "room_name": room_name
    })
