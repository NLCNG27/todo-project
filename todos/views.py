from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo


# Create your views here.
class HomePageView(ListView):
    model = Todo
    template_name = 'home.html'


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = ['text']

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')