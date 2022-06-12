from email import message
from django.shortcuts import render, redirect
from .models import Usuario, RolUsuario, Comida
from django.contrib import messages

# Create your views here.

def menu(request):
    return render(request,'Web/menu.html')

def test(request):
    return render(request,'Web/test.html')

def Registrarse(request):
    return render(request,'Web/Registrarse.html')



def registrarUsuario(request):
    nombre2     = request.POST['nomUser']
    apellido2   = request.POST['apeUser']
    email2      = request.POST['email']
    contra2     = request.POST['password1']

    try:
        c = Usuario.objects.get(email = email2)
        c1 = False
    except Usuario.DoesNotExist:
        c1 = True      
    
    if c1 == True:
        messages.error(request, 'Cargando')
        Usuario.objects.create(nomUsuario = nombre2, apellido = apellido2, email = email2, contrasena = contra2)
        sesion = Usuario.objects.get(nomUsuario=nombre2)
        contexto ={
        "sesion":sesion
        }
        messages.success(request, 'Cuenta registrada')
        return render(request,"Recetas/menu.html",contexto)
    else:
        messages.error(request, 'El correo ya esta ocupado')
        return redirect ('Registrarse')
