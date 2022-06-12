from django.contrib import admin
from .models import Usuario, Comida, RolUsuario

# Register your models here.

admin.site.register(RolUsuario)
admin.site.register(Usuario)
admin.site.register(Comida)
