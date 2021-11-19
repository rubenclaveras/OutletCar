from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import View
from .models import CategoriaCoche, Coche, Marca, Categoria

def index(request):
    coches = Coche.objects.all()
    categorias = Categoria.objects.all()
    categoriasCoche = CategoriaCoche.objects.all()
    marcas = Marca.objects.all()
    for marca in marcas:
        marca.coches = Coche.objects.order_by('precio').filter(
        marca= marca.pk).all()[:1]
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
        return render (request, 'marcas.html', contexto)

class CategoriaVista(View):
    def get(self, request, slug_categoria):
        categoria= get_object_or_404(Categoria, slug=slug_categoria)
        coches = Coche.objects.all()
        categorias = Categoria.objects.all()
        categoriasCoche = CategoriaCoche.objects.all()
        marcas = Marca.objects.all()
        contexto = {
            'coches':coches,
            'categorias': categorias,
            'categoriasCoche': categoriasCoche,
            'marcas': marcas,
            'categoria': categoria,
        }
        return render (request, 'categorias.html', contexto)

class AnuncioVista(View):
    def get(self, request, slug_coche):
        coche= get_object_or_404(Coche, slug=slug_coche)
        coches = Coche.objects.all()
        categorias = Categoria.objects.all()
        categoriasCoche = CategoriaCoche.objects.all()
        marcas = Marca.objects.all()
        contexto = {
            'coches':coches,
            'categorias': categorias,
            'categoriasCoche': categoriasCoche,
            'marcas': marcas,
            'coche': coche,
        }
        return render (request, 'anuncios.html', contexto)