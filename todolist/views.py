from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from todolist.models import Todo

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Todo

class ImpressumView(TemplateView):
    template_name = 'impressum.html'

class AddView(CreateView):
    template_name = 'add.html'
    model = Todo
    fields = ['title','deadline','progress']
    success_url = '/'

class UpdateView(UpdateView):
    template_name = 'edit.html'
    model = Todo
    fields = ['title','deadline','progress']
    success_url = '/'

