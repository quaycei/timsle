from django.conf.urls import url
from timsle import views

urlpatterns = [
    url(r'^land/$', views.timsle_lander, name='timsle_lander'),

 ]