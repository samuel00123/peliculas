from django.db import models
from django.utils import timezone
from django.contrib import admin

class Libro(models.Model):
    isbn= models.CharField(max_length=14)
    titulo = models.CharField(max_length=200)
    portada= models.ImageField(upload_to='media/fotos',null=True,blank=True)
    autor=models.CharField(max_length=50)
    editorial=models.CharField(max_length=50)
    pais=models.CharField(max_length=60)
    aniopub = models.IntegerField()

def __str__(self):
    return self.titulo

class Usuarios(models.Model):
    dpi=models.CharField(max_length=20)
    nombre=models.CharField(max_length=60)
    prestamo=models.ManyToManyField(Libro)


def __str__(self):
    return self.nombre

class Prestamos(models.Model):
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo=models.DateTimeField(blank=True, null=True)
    fecha_devolucion_propuesta=models.DateTimeField(blank=True, null=True)
    fecha_devolucion_real=models.DateTimeField(blank=True, null=True)


class PrestamosInLine(admin.TabularInline):
    model = Prestamos
    extra = 1

class UsuariosAdmin(admin.ModelAdmin):
    inlines = (PrestamosInLine,)

class LibroAdmin (admin.ModelAdmin):
    inlines = (PrestamosInLine,)
