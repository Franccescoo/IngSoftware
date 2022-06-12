from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'Web/index.html')

def menu(request):
    return render(request,'Web/menu.html')

def test(request):
    return render(request,'Web/test.html')

def Registrarse(request):
    messages.success(request, 'Cuenta registrada')
    return render(request,'Web/Registrarse.html')