from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoapp.models import Tasks
from todoapp.forms import TaskCreateForm,TaskSearch,TaskUpdateForm

# Create your views here.
#task creation:=>html,view

def create_task(request):
    if request.method=='GET':
        form = TaskCreateForm()
        task = Tasks.objects.all()
        context = {}
        context['tasks'] = task
        context['form'] = form
        return render(request, 'todoapp/create_task.html', context)
    else:
        form = TaskCreateForm(request.POST)
        if form.is_valid():

            task_name = form.cleaned_data.get('task_name')
            date = form.cleaned_data.get('date')
            status = form.cleaned_data.get('status')
            obj = Tasks(task_name=task_name, date=date, status=status)
            obj.save()
            print('saved==========')
            task = Tasks.objects.all()
            context = {}
            context['tasks'] = task
            form = TaskCreateForm()
            context['form'] = form
            return render(request, 'todoapp/create_task.html', context)

# def addTask(request):
#     my_task = request.POST.get('task')
#     date = request.POST.get('date')
#     status = request.POST.get('status')
#     obj = Tasks(task_name=my_task,date=date,status=status)
#     obj.save()
#     # print('saved==========')
#     task = Tasks.objects.all()
#     context = {}
#     context['tasks']=task
#     return render(request,'todoapp/create_task.html',context)



def get_task_search(request):
    if request.method=='GET':
        form = TaskSearch()
        context = {}
        context['form']=form
        return render(request, 'todoapp/taskSearch.html', context)
    else:
        form = TaskSearch(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            tasks = Tasks.objects.filter(date=date)
            form = TaskSearch()
            context = {}
            context['tasks'] = tasks
            context['form'] = form
        return render(request,'todoapp/taskSearch.html',context)


def date_search(request):
    date = request.POST.get('date')
    tasks = Tasks.objects.filter(date=date)
    context = {}
    context['tasks'] = tasks
    return render(request,'todoapp/taskSearch.html',context)

def delete_task(request,id):
    task = Tasks.objects.get(id=id)
    task.delete()
    return redirect('create')

def task_update(request,id):
    task = Tasks.objects.get(id=id)
    """id = forms.CharField(max_length=12)
    task_name = forms.CharField(max_length=120)
    date = forms.CharField(max_length=50)
    status = forms.CharField(max_length=60)"""
    initial_data={
        'id' : task.id,
        'task_name':task.task_name,
        'date':task.date,
        'status':task.status
    }
    form = TaskUpdateForm(initial=initial_data)
    context={}
    context['tasks'] = task
    context['form'] = form
    if request.method=='POST':
        form = TaskUpdateForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            task_name = form.cleaned_data.get('task_name')
            date = form.cleaned_data.get('date')
            status = form.cleaned_data.get('status')

            task = Tasks.objects.get(id=id)
            task.task_name = task_name
            task.date = date
            task.status = status
            task.save()
            return redirect('create')
    return render(request,'todoapp/task_update.html',context)

