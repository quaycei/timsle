from django.conf.urls import url

from pact import views


urlpatterns = [
    url(r'^list', views.pact_list, name='pact_list'),
    url(r'^pact/(?P<pact_id>[\w-]+)/$', views.pact_read, name='pact_read'),
    url(r'(?P<pact_id>[\w-]+)/buddy/new', views.buddy_create, name='buddy_create'),
    url(r'^buddy/(?P<buddy_id>[\w-]+)/status', views.buddy_status, name='buddy_status'),
    url(r'(?P<pact_id>[\w-]+)/checkin', views.pact_checkin, name='pact_checkin'),
]
