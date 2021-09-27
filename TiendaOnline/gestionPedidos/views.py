from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
def busqueda_productos(request):
    return render(request, "index.html")

def buscar(request):
    #Si el usuario manda el formulario vacio
    if request.GET["prd"]:
       producto=request.GET['prd']

       articulos=Articulos.objects.filter(nombre__icontains=producto)

       return render(request, "resultado_busqueda.html", {'articulos':articulos, 'query':producto})
    else:
        mensaje="Para obtener un resultado debes introducir el nombre del producto"

    return HttpResponse(mensaje)