from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def busqueda_productos(request):
    return render(request, "index.html")

def buscar(request):
    #Si el usuario manda el formulario vacio
    if request.GET["prd"]:
        producto=request.GET["prd"]

        #Limitar caracteres de busqueda
        if len(producto)>20:
            mensaje="Texto demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {'articulos':articulos, 'query':producto})
    else:
        mensaje="Para obtener un resultado debes introducir el nombre del producto"

    return HttpResponse(mensaje)


#Formulario de Contacto
def contacto(request):  
    #En caso que detecte el post
    if request.method=="POST":

        subject=request.POST["consulta"]

    #Recuperar datos del usariio
        message=request.POST["mensaje"] + "" + request.POST["email"]
       
        email_from=settings.EMAIL_HOST_USER
    #Donde viaja la consulta
    recipient_list=["ic.chamorro07@gmail.com"]

    send_mail(subject, message, email_from, recipient_list)

    return render(request, "saludos.html")
        
    return render(request, "formcontacto.html")