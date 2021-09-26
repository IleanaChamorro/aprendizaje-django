from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def busqueda_productos(request):
    return render(request, "index.html")

def search(request):
    mensaje="Busqueda Articulo: %r" %request.GET['producto']

    return HttpResponse(mensaje)