from django.shortcuts import render, redirect
import requests

# Create your views here.
def home(request):
    return render(request,'index.html')

def productos(request):
    return render(request,'Productos.html')

def instalaciones(request):
    return render(request,'Instalaciones.html')

def contacto(request):
    return render(request,'contacto.html')

def developer(request):
    return render(request,'Developer.html')