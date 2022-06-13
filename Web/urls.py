from unicodedata import name
from django.urls import URLPattern, path
from .views import  menu, Listar_Usuario, Registrarse, registrarUsuario, eliminar_usuario
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',menu,name="menu"),
    path('menu',menu,name="menu"),
    path('Listar_Usuario',Listar_Usuario,name="Listar_Usuario"),
    path('Registrarse',views.Registrarse,name="Registrarse"),
    path('eliminar_usuario',eliminar_usuario, name="eliminar_usuario"),


    path('registrarUsuario', views.registrarUsuario, name="registrarUsuario"),

]