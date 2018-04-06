from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from SOSBicho import settings
from . import views



urlpatterns = [
    url(r'^SOSBicho/$', views.index, name="index"),
    url(r'^SOSBicho/new$', views.newAnimal, name="newAnimal"),
    url(r'^SOSBicho/edit/(?P<idAnimal>\d+)$', views.editAnimal, name="editAnimal"),
    url(r'^SOSBicho/take/(?P<idAnimal>\d+)$', views.takeAnimal, name="takeAnimal"),
    url(r'^SOSBicho/del/(?P<idAnimal>\d+)$', views.delAnimal, name="delAnimal"),

    url(r'^SOSBicho/login', views.loginView, name="loginView"),
    url(r'^SOSBicho/logout', auth_views.logout, {'next_page': 'loginView'}, name="logoutView"),

    url(r'^SOSBicho/user/new/$', views.newUser,  name="newUser"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)