from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room,Message
from django.contrib.auth.models import User
# Create your views here.
@login_required
def show_rooms(request):
    rooms=Room.objects.filter(is_group=True)
    return render(request, 'rooms.html',{'rooms':rooms})
@login_required
def show_room(request,slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)
    return render(request, 'room.html',{'room':room,'messages':messages})

@login_required
def all_users(request):
    users=User.objects.exclude(username=request.user.username)
    print(users)
    return render(request, 'user.html',{'users':users})
@login_required
def contact(request, username):
    user1=User.objects.get(username=username).username
    user2=request.user.username
    name=""
    if user1>user2:
        name= str(user1) + str(user2)
    else:
        name= str(user2) + str(user1)
    if not Room.objects.filter(slug=name):
        print("not exist")
        Room.objects.create(name=name, slug=name,is_group=False)
        room=Room.objects.get(slug=name)
        messages=Message.objects.filter(room=room)[0:25]
    room=Room.objects.get(slug=name)
    messages=Message.objects.filter(room=room)[0:25]
    return render(request, 'room.html', {'room':room,'messages':messages})
