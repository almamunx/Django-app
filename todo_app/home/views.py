from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelform_factory

from home.models import Todo

# Create your views here.
def index(request):
     return render(request, "home/index.html", {"tasks" : Todo.objects.count()})


def task(request):
     form = modelform_factory(Todo, exclude=[])
     return render(request, "home/create_task.html", {"form" : form})

     