from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.forms import modelform_factory

from home.models import Todo

# Create your views here.
# Class based view

class HomePageView(TemplateView):

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['taskList'] = Todo.objects.all()
         return context


class TaskView(View):
     form_class = modelform_factory(Todo, exclude=[])
     initial = {'key': 'value'}
     template_name = "home/task_create.html"
     
     def get(self, request, *args, **kwargs):
          print(kwargs)
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form': form})

     def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class TaskDetailView(DetailView):
     model = Todo
     template_name = "home/task_details.html"
     context_object_name = 'task'
     pk_url_kwarg = "slug"
     
     def get_object(self, *args, **kwargs):
          context = get_object_or_404(Todo, url = self.kwargs.get("slug"))
          return context



# def index(request):
#      tasks = Todo.objects.all()
#      return render(request, "home/index.html", {"tasks" : tasks})


# def task(request):
#      TaskForm = modelform_factory(Todo, exclude=[])
#      if request.method == "POST":
#           form = TaskForm(request.POST)
#           if form.is_valid():
#                form.save()
#                response = redirect('/')
#                return response

#      else:
#           form = TaskForm()
#      return render(request, "home/task_create.html", {"form" : form})


# def task_details(request, id):
#      task = get_object_or_404(Todo, pk=id)
#      return render(request, "home/task_details.html", {"task": task})


# def task_update(request, pk):
#      task = Todo.objects.get(id=pk)
#      modelForm = modelform_factory(Todo, exclude=[])
#      TaskForm = modelForm(instance=task)

#      if request.method == 'POST':
#           form = modelForm(request.POST, instance=task)
#           if form.is_valid():
#                form.save()
#                return redirect('/')

#      return render(request, "home/task_create.html", {"form" : TaskForm})


# def task_delete(request, id):
#      task = get_object_or_404(Todo, pk=id)
#      task.delete()
#      return redirect('/')