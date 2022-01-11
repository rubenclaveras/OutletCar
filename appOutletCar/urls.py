from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/<slug:slug_categoria>', views.CategoriaVista.as_view(), name='categoria'),
    path('marcas/<slug:slug_marca>', views.MarcaVista.as_view(), name='marca'),
    path('anuncios/<slug:slug_coche>', views.AnuncioVista.as_view(), name='anuncio'),
    path('busquedaCoches/', views.busquedaCoches),
    path('buscar/', views.buscar),
]