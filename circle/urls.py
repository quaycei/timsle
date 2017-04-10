from django.conf.urls import url
from circle import views

urlpatterns = [
    url(r'^list/$', views.circle_list, name='circle_list'),
    url(r'^menu/$', views.circle_menu, name='circle_menu'),
    url(r'^circle/(?P<circle_id>[\w-]+)/$', views.circle_list, name='circle_list'),
    url(r'^project/(?P<project_id>[\w-]+)/$', views.project_read, name='project_read'),
    url(r'^challenge/(?P<project_id>[\w-]+)/(?P<content_id>[\w-]+)/$', views.content_read, name='content_read'),
]

