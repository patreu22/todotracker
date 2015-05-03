from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView
from todolist.models import Todo

# Create your views here.
class IndexView(ListView):
    template_name = 'todolist/index.html'
    model = Todo

class CreateView(CreateView):
    template_name = 'todolist/create.html'
    model = Todo
    fields = ['title','deadline','progress']
    success_url = '/'
