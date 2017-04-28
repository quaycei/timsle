from django.conf.urls import url
from palette import views


urlpatterns = [
    url(r'^(?P<palette_id>[\w-]+)/update/$', views.palette_update, {}, 'palette_update'),
    url(r'^registry/(?P<registry_id>[\w-]+)/palette/create/$', views.palette_create, {}, 'palette_create'),
]

