from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
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
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form': form})

     def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})