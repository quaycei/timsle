from django.conf.urls import url
from registry import views


urlpatterns = [
    url(r'^registry_list/$', views.registry_list, name='registry_list'),
    url(r'^registry/create/$', views.registry_create, {}, 'registry_create'),
    url(r'^registry/(?P<registry_id>[\w-]+)/update/$', views.registry_update, {}, 'registry_update'),
    url(r'^registry/(?P<registry_id>[\w-]+)/$', views.registry_dashboard, name='registry_dashboard'),
    url(r'^contact/(?P<contact_id>[\w-]+)/$', views.contact_read, {}, 'contact_read'),
    url(r'^contact/(?P<contact_id>[\w-]+)/update/$', views.contact_update, {}, 'contact_update'),
    url(r'^registry/(?P<registry_id>[\w-]+)/contact/create/$', views.contact_create, {}, 'contact_create'),
]

