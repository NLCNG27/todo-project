# todos/models.py
from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('home')
