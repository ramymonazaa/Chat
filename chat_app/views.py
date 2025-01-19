from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
# Create your views here.
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
def frontpage(request):
    users=User.objects.exclude(username=request.user.username)
    if request.user.is_authenticated:
        return render(request, 'frontpage.html',{'users':users})
    else:
        return render(request, 'frontpage.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('frontpage')
    else:
        form=SignUpForm()
    return render(request,'signup.html',{'form':form})   


        