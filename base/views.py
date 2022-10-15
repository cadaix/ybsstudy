from django.shortcuts import render

from .models import Room
from .forms import RoomForm


# rooms = [
#     {'id':1,
#     'name':'İşletme Giriş'
#     },
#       {'id':2,
#     'name':'İşletme Matematiği'
#     },
#       {'id':3,
#     'name':'Programlamaya Giriş'
#     },
#       {'id':4,
#     'name':'İşletme Bilimine Giriş'
#     },
#       {'id':5,
#     'name':'Bilgisayar Kullanımına Giriş'
#     },
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room' : room}

    return render(request, 'base/room.html', context) 

def createRoom(request):
    form = RoomForm
    context = {'form' : form }
    return render(request,'base/room_form.html', context)
     
