from django.shortcuts import render
from inicio.models import Perro

# Create your views here.
def inicio(request):
    
    diccionario = {
        'mensaje': 'Esto es un mensaje de inicio...'
    }
 
    return render(request, 'inicio.html', diccionario)

def crear_perro(request, nombre, edad):
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
        'perro': perro
    }
    return render(request, 'inicio.html', diccionario)