from email import message
from django.shortcuts import render, redirect
from .models import Usuario, RolUsuario, Comida
from django.contrib import messages

# Create your views here.

def menu(request):
    return render(request,'Web/menu.html')

def Listar_Usuario(request):
    return render(request,'Web/Listar_Usuario.html')

def Registrarse(request):
    return render(request,'Web/Registrarse.html')

def test(request):
    return render(request,'Web/test.html')

def Login(request):
    return render(request,'Web/Login.html')

def Vista_Usuario(request,id):
    sesion = Usuario.objects.get(idUsuario=id)
    contexto={
        "sesion":sesion
    }
    return render(request,'Web/Vista_Usuario.html',contexto)

def Vista_Admin(request,sesion):

    contexto={
        "sesion":sesion
    }
    return render(request,'Web/Vista_Admin.html',contexto)

#def inicioUser(request,sesion):

    contexto={
        "sesion":sesion
    }
    return render(request,'Recetas/inicioUser.html',contexto)


# Vistas de Usuarios 

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
        Usuario.objects.create(nomUsuario = nombre2, apellido = apellido2, email = email2, contrasena = contra2)

        sesion = Usuario.objects.get(nomUsuario=nombre2)
        contexto ={
        "sesion":sesion
        }
        messages.success(request, 'Cuenta registrada')
        return render(request,"Web/Registrarse.html",contexto)
    else:
        messages.error(request, 'El correo ya esta ocupado')
        return redirect ('Registrarse')



def listadoUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {"lista_u":usuario}
    return render(request,"Web/Listar_Usuario.html", contexto)



def Listar_Usuario(request):
    UserAdmin = Usuario.objects.all()
    contexto = {
        "usuario":UserAdmin,
        }
    return render(request,'Web/Listar_Usuario.html',contexto)



def eliminar_usuario(request,id,sesi):
    usuar = Usuario.objects.get(idUsuario = id)
    usuar.delete() #Elimina registro
    messages.success(request,'Usuario Eliminado')

    x = Usuario.objects.get(idUsuario=sesi)
    rol2 = RolUsuario.objects.get(nomRol = 'Administrador')

    if x.RolUsuario.nomRol == rol2.nomRol:
        contexto ={"sesion":x}
        return render(request, 'Web/Listar_Usuario.html',contexto)
    else:
        contexto ={"sesion":x}
        return render(request, 'Web/Listar_Usuario.html',contexto)
