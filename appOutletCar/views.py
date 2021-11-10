from django.shortcuts import render
from django.http import HttpResponse
from .models import Coche, Categoria

def index(request):
    coches = Coche.objects.all()
    categorias = Categoria.objects.all()
    contexto = {
        'coches':coches,
        'categorias': categorias
    }
    return render(request, 'index.html', contexto)