from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'todolist/index.html'
