from unicodedata import name
from django.urls import URLPattern, path
from .views import index, menu, test

urlpatterns = [
    path('',index,name="index"),
    path('menu',menu,name="menu"),
    path('test',test,name="test"),

]