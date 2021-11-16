from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import View
from .models import CategoriaCoche, Coche, Marca, Categoria

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

class MarcaVista(View):
    def get(self, request, slug_marca):
        coches = Coche.objects.all()
        categorias = Categoria.objects.all()
        categoriasCoche = CategoriaCoche.objects.all()
        marcas = Marca.objects.all()
        marca= get_object_or_404(Marca, slug=slug_marca)
        contexto = {
            'coches':coches,
            'categorias': categorias,
            'categoriasCoche': categoriasCoche,
            'marcas': marcas,
            'marca': marca,
        }
        return render (request, 'marca.html', contexto)

class CategoriaVista(View):
    def get(request, slug_categoria):
        coches = Coche.objects.all()
        categorias = Categoria.objects.all()
        categoriasCoche = CategoriaCoche.objects.all()
        marcas = Marca.objects.all()
        categoria= get_object_or_404(Categoria, slug=slug_categoria)
        contexto = {
            'coches':coches,
            'categorias': categorias,
            'categoriasCoche': categoriasCoche,
            'marcas': marcas,
            'categoria': categoria,
        }
        return render (request, 'categoria.html', contexto)
