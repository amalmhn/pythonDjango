from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#task creation:=>html,view

def create_task(request):
    return render(request,'todoapp/create_task.html')

def addTask(request):
    my_task = request.POST.get('task')
    print(my_task)
    return HttpResponse('<h1>AddYourTaskView</h1>')