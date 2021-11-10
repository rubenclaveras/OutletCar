from django.shortcuts import render
from django.http import HttpResponse
from .models import CategoriaCoche, Coche, Categoria

def index(request):
    coches = Coche.objects.all()
    categorias = Categoria.objects.all()
    categoriasCoche = CategoriaCoche.objects.all()
    contexto = {
        'coches':coches,
        'categorias': categorias,
        'categoriasCoche': categoriasCoche,
    }
    return render(request, 'index.html', contexto)