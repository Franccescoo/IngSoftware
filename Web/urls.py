from unicodedata import name
from django.urls import URLPattern, path
from .views import  menu, confirmar, pedidos, Listar_Usuario, metodo, menu_usuario, stock_admin, direccion_usuario, Login, login_app, Registrarse, registrarUsuario, eliminar_usuario, test, Vista_Usuario, Vista_Admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',menu,name="menu"),
    path('menu',menu,name="menu"),
    path('menu_usuario',menu_usuario,name="menu_usuario"),
    path('confirmar',confirmar,name="confirmar"),
    path('metodo',metodo,name="metodo"),
    path('pedidos',pedidos,name="pedidos"),
    path('Listar_Usuario',Listar_Usuario,name="Listar_Usuario"),
    path('Registrarse',views.Registrarse,name="Registrarse"),
    path('test',test,name="test"),
    path('Login',Login,name="Login"),
    path('Vista_Usuario',Vista_Usuario,name="Vista_Usuario"),
    path('Vista_Admin',Vista_Admin,name="Vista_Admin"),
    path('direccion_usuario',direccion_usuario,name="direccion_usuario"),
    path('stock_admin',stock_admin,name="stock_admin"),

    path('eliminar_usuario',eliminar_usuario, name="eliminar_usuario"),
    path('registrarUsuario', views.registrarUsuario, name="registrarUsuario"),
    path('login_app', login_app, name="login_app"),

]