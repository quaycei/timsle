from django.conf.urls import url
from circle import views

urlpatterns = [
    url(r'^list/$', views.circle_list, name='circle_list'),
    url(r'^menu/$', views.circle_menu, name='circle_menu'),
    url(r'^groups/$', views.group_list, name='group_list'),
    url(r'^(?P<group_slug>[\w-]+)/projects/$', views.project_list, name='project_list'),
    url(r'^org/(?P<organization_slug>[\w-]+)/$', views.organization_read, name='organization_read'),
    url(r'^(?P<circle_slug>[\w-]+)/$', views.circle_read, name='circle_read'),
    url(r'^(?P<circle_slug>[\w-]+)/(?P<project_id>[\w-]+)/$', views.project_read, name='project_read'),
    url(r'^challenge/(?P<project_id>[\w-]+)/(?P<content_id>[\w-]+)/$', views.content_read, name='content_read'),
]

