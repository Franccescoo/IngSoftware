from unicodedata import name
from django.urls import URLPattern, path
from .views import index

urlpatterns = [
    path('',index,name="index"),

]