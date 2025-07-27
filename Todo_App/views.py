from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def home(request):
    task = Task.objects.filter(isCompleted=False).order_by('-id')
    completedTasks = Task.objects.filter(isCompleted=True).order_by('-id')
    context = {
        'task': task,
        'completedTasks': completedTasks,
    }
    return render(request, 'home.html', context)
def addtask(request):
    if request.method == 'POST':
        name = request.POST.get('taskname')

        task = Task(
            TaskName=name,
        )
        task.save()
        return redirect('home')
    return render(request, 'home.html')
def marks_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted=True
    task.save()
    return redirect('home')
def marks_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted=False
    task.save()
    return redirect('home')
def edittask(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('taskname')
        task.TaskName=name
        task.save()
        return redirect('home')
    else:
        context = {
            'get_task': task,
        }
        return render(request, 'edittask.html', context)
def deletetask(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')



