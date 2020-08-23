
from django.contrib import admin
from django.urls import path, include

from home.views import HomePageView, TaskView, TaskDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
]
    # path('', index),
    # path('task', task),
    # path('task/<int:id>', task_details),
    # path('task_update/<int:pk>', task_update),
    # path('task_delete/<int:id>', task_delete)