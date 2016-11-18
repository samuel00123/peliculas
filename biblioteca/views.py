from django.shortcuts import render, get_object_or_404
from .models import Libro
from .forms import LibroForm
from django.contrib import messages

def postear_libros(request):
    posts= Libro.objects.all()
    return render(request, 'biblioteca/postear_libro.html', {'posts': posts})


def post_new(request):
        if request.method == "POST":
            form = LibroForm(request.POST)
            libro = Libro.objects.create(isbn=form.cleaned_data['isbn'], titulo = form.cleaned_data['titulo'], portada = form.cleaned_data['portada'], autor = form.cleaned_data['autor'], editorial = form.cleaned_data['editoria'], pais = form.cleaned_data['pais'],aniopub = form.cleaned_data['aniopub'])
            libro.save()
        else:
            form = LibroForm()
        return render(request, 'biblioteca/editar_libro.html', {'form': form})
        messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
