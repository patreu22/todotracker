from django.conf.urls import patterns, url
from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add', views.AddView.as_view(), name='add'),
    url(r'^impressum', views.ImpressumView.as_view(), name='impressum'),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='todo_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='todo_delete'), 
)
