from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import modelform_factory

from home.models import Todo

# Create your views here.
def index(request):
     tasks = Todo.objects.all()
     return render(request, "home/index.html", {"tasks" : tasks})


def task(request):
     TaskForm = modelform_factory(Todo, exclude=[])
     if request.method == "POST":
          form = TaskForm(request.POST)
          if form.is_valid():
               form.save()
               response = redirect('/')
               return response

     else:
          form = TaskForm()
     return render(request, "home/task_create.html", {"form" : form})


def task_details(request, id):
     task = get_object_or_404(Todo, pk=id)
     return render(request, "home/task_details.html", {"task": task})


def task_update(request, pk):
     task = Todo.objects.get(id=pk)
     modelForm = modelform_factory(Todo, exclude=[])
     TaskForm = modelForm(instance=task)

     if request.method == 'POST':
          form = modelForm(request.POST, instance=task)
          if form.is_valid():
               form.save()
               return redirect('/')

     return render(request, "home/task_create.html", {"form" : TaskForm})


def task_delete(request, id):
     task = get_object_or_404(Todo, pk=id)
     task.delete()
     return redirect('/')