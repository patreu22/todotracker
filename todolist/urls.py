from django.conf.urls import patterns, url
from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create$', views.CreateView.as_view(), name='create'), 
)
