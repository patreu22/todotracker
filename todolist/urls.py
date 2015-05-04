from django.conf.urls import patterns, url
from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add', views.AddView.as_view(), name='add'), 
)
