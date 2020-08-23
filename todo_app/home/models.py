from django.urls import reverse
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, unique=True, default="hello")
    description = models.CharField(max_length=200)
    date = models.DateField()
    is_Complete = models.BooleanField()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:task_details", kwargs={"slug": self.url})
