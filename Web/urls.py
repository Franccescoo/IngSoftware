from unicodedata import name
from django.urls import URLPattern, path
from .views import  menu, Listar_Usuario, Login, Registrarse, registrarUsuario, eliminar_usuario, test, Vista_Usuario, Vista_Admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',menu,name="menu"),
    path('menu',menu,name="menu"),
    path('Listar_Usuario',Listar_Usuario,name="Listar_Usuario"),
    path('Registrarse',views.Registrarse,name="Registrarse"),
    path('test',test,name="test"),
    path('Login',Login,name="Login"),
    path('Vista_Usuario/<int:id>',views.Vista_Usuario,name="Vista_Usuario"),
    path('Vista_Admin/<int:id>',views.Vista_Admin,name="Vista_Admin"),

    path('eliminar_usuario',eliminar_usuario, name="eliminar_usuario"),
    path('registrarUsuario', views.registrarUsuario, name="registrarUsuario"),

]