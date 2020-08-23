
from django.contrib import admin
from django.urls import path
from home.views import HomePageView, TaskView, TaskDetailView

app_name = "home"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('task/', TaskView.as_view(), name='task_view'),
    path('task/<str:slug>', TaskDetailView.as_view(), name='task_details'),
]