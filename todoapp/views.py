from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import Tasks
# Create your views here.
#task creation:=>html,view

def create_task(request):
    task = Tasks.objects.all()
    context = {}
    context['tasks'] = task
    return render(request, 'todoapp/create_task.html', context)

def addTask(request):
    my_task = request.POST.get('task')
    date = request.POST.get('date')
    status = request.POST.get('status')
    obj = Tasks(task_name=my_task,date=date,status=status)
    obj.save()
    # print('saved==========')
    task = Tasks.objects.all()
    context = {}
    context['tasks']=task
    return render(request,'todoapp/create_task.html',context)

def get_task_search(request):
    return render(request,'todoapp/taskSearch.html')

def date_search(request):
    date = request.POST.get('date')
    tasks = Tasks.objects.filter(date=date)
    context = {}
    context['tasks'] = tasks
    return render(request,'todoapp/taskSearch.html',context)