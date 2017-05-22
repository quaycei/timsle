from django.conf.urls import url
from timsle import views

urlpatterns = [
    url(r'^start/$', views.timsle_lander, name='timsle_lander'),

 ]