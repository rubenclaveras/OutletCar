from django.shortcuts import render
from django.http import HttpResponse
from .models import CategoriaCoche, Coche, Categoria, Marca

def index(request):
    coches = Coche.objects.all()
    categorias = Categoria.objects.all()
    categoriasCoche = CategoriaCoche.objects.all()
    marcas = Marca.objects.all()
    contexto = {
        'coches':coches,
        'categorias': categorias,
        'categoriasCoche': categoriasCoche,
        'marcas': marcas,
    }
    return render(request, 'index.html', contexto)