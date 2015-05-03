from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView
from todolist.models import Todo

# Create your views here.
class IndexView(ListView):
    template_name = 'todolist/index.html'
    model = Todo
