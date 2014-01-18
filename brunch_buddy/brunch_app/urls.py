from django.conf.urls import patterns, url

from brunch_app import views

urlpatterns = patterns('',
    #index
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<restaurant_id>\d+)/$', views.detail, name='detail'),
    url(r'^add.html', views.add, name='add'),
    url(r'^(?P<restaurant_id>\d+)/confirm.html$', views.confirm, name='confirm'),
    url(r'^(?P<restaurant_id>\d+)/', views.edit, name='edit'),
    
)