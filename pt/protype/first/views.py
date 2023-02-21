from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import customizeRegistList
from .models import teacherChart
from .forms import pic_Form
from .models import Picture
# Create your views here.

def mainPage(request):
    return render(request, 'first/home.html')

def logIn(request):
    if request.method == 'POST':
       user = authenticate(request, username = request.POST['Username'], password = request.POST['Passwords'])
       if user is None:
           return render(request, 'first/login.html', {'error':'incorrect username or passwords'})
       else:
            login(request, user)
            return redirect('first:MainPage')
    else:
        return render(request, 'first/login.html')
    
def logOut(request):
    logout(request)
    return redirect('first:MainPage')

def regist(request):
    if request.method == 'POST':
        registList = customizeRegistList(request.POST)
        if registList.is_valid():
            registList.save()
            user = authenticate(username = registList.clean_data['username'], password = registList.clean_data['password1'])
            teacherChart(AuburnID = registList.clean_data['AuburnID']).save()
            login(request, user)
            return redirect('first:MainPage')
    else:
        registList = customizeRegistList()
    detail = {'registList' : registList}
    return render(request, 'first/register.html', detail)

def pic_upload(request):
    if request.method == 'POST':
        form = pic_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('first:Pic_upload')
    else:
        form = pic_Form()
    pictures = Picture.objects.all()
    return render(request, 'first/pic_upload.html', {'form': form})

def pic_show(request):
    pictures = Picture.objects.all()
    return render(request, 'first/pic_show.html', {'pictures': pictures})