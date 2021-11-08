from django.shortcuts import render
from django.http import HttpResponse
from .models import Coche

def index(request):
    return render(request, 'index.html')