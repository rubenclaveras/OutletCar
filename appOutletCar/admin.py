from django.contrib import admin
from .models import CategoriaCoche, Coche, Categoria, Marca

admin.site.register(Coche)
admin.site.register(Categoria)
admin.site.register(CategoriaCoche)
admin.site.register(Marca)
