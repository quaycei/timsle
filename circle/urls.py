from django.conf.urls import url
from circle import views

urlpatterns = [
    url(r'^list/$', views.circle_list, name='circle_list'),
    url(r'^menu/$', views.circle_menu, name='circle_menu'),
    url(r'^mothership/$', views.group_list, name='group_list'),
    url(r'^circle/(?P<circle_id>[\w-]+)/$', views.circle_list, name='circle_list'),
    url(r'^project/(?P<project_id>[\w-]+)/$', views.project_read, name='project_read'),
    url(r'^challenge/(?P<project_id>[\w-]+)/(?P<content_id>[\w-]+)/$', views.content_read, name='content_read'),
    url(r'^project/(?P<project_id>[\w-]+)/update/$', views.project_update, {}, 'project_update'),
    url(r'^registry/(?P<registry_id>[\w-]+)/project/create/$', views.project_create, {}, 'project_create'),
    url(r'^circle/(?P<circle_id>[\w-]+)/update/$', views.circle_update, {}, 'circle_update'),
    url(r'^registry/(?P<registry_id>[\w-]+)/circle/create_user/$', views.circle_create_user, {}, 'circle_create_user'),
    url(r'^registry/(?P<registry_id>[\w-]+)/circle/create_offering/$', views.circle_create_offering, {}, 'circle_create_offering'),
    url(r'^registry/(?P<registry_id>[\w-]+)/circle/(?P<circle_id>[\w-]+)/create/types$', views.circle_create_types, {}, 'circle_create_types'),
    url(r'^link/(?P<link_id>[\w-]+)/update/$', views.link_update, {}, 'link_update'),
    url(r'^registry/(?P<registry_id>[\w-]+)/link/create/$', views.link_create, {}, 'link_create'),



]

