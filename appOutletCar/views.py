from django.shortcuts import render
from django.http import HttpResponse
from .models import Coche

def index(request):
    coches = Coche.objects.all()
    contexto = {
        'coches':coches
    }
    return render(request, 'index.html', contexto)