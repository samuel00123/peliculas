from django.contrib import admin
from .models import Libro, Usuarios,Prestamos

admin.site.register(Libro)
admin.site.register(Usuarios)
admin.site.register(Prestamos)
