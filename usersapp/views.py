from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'usersapp/login.html')

def registration(request):
    return render(request,'usersapp/registration.html')
