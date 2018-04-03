from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^SOSBicho/$', views.index, name="index"),

    url(r'^SOSBicho/login', views.loginView, name="loginView"),
    url(r'^SOSBicho/logout', auth_views.logout, {'next_page': 'logoutView'}, name="logoutView"),



    ]