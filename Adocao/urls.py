from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^SOSBicho/$', views.index, name="index"),
    ]