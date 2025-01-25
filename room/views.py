from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.contrib.auth.models import User
from .forms import RoomForm

# Create your views here.
@login_required
def show_rooms(request):
    rooms=Room.objects.filter(is_group=True , members=request.user)
    return render(request, 'rooms.html',{'rooms':rooms})
@login_required
def show_room(request,slug):
    print(slug)
    if Room.objects.filter(slug=slug):
        room=Room.objects.get(slug=slug)
        messages=Message.objects.filter(room=room)
        return render(request, 'room.html',{'room':room,'messages':messages})
    return redirect('rooms')

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
        name= str(user1)+"_" + str(user2)
    else:
        name= str(user2)+"_" + str(user1)
    if not Room.objects.filter(slug=name):
        print("not exist")
        Room.objects.create(name=name, slug=name,is_group=False)
        room=Room.objects.get(slug=name)
        room.members.add(request.user)  # Add the logged-in user
        room.members.add(User.objects.get(username=username))  # Add the specified user
        room=Room.objects.get(slug=name)
        messages=Message.objects.filter(room=room)[0:25]
    room=Room.objects.get(slug=name)
    messages=Message.objects.filter(room=room)[0:25]
    return render(request, 'room.html', {'room':room,'messages':messages})
# @login_required
    
def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST, user=request.user)
        if form.is_valid():
            room = form.save()
            # Add selected users as members
            room.members.set(form.cleaned_data['members'])
            room.members.add(request.user)
            room.slug=str(room.id)
            room.save()
            return redirect('rooms')  # Replace 'rooms' with the name of your rooms list URL
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})
