from unicodedata import name
from django.urls import URLPattern, path
from .views import  menu, test, Registrarse, registrarUsuario
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',menu,name="menu"),
    path('menu',menu,name="menu"),
    path('test',test,name="test"),
    path('Registrarse',views.Registrarse,name="Registrarse"),


    path('registrarUsuario', views.registrarUsuario, name="registrarUsuario"),

]