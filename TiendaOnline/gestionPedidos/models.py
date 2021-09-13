from django.db import models

# Create your models here.

#Los modelos determinan como va a ser la estructura de la base de datos
#Creacion de una clase por cada tabla que necesites que tenga tu base de datos
class Clientes(models.Model):
    #Campos que tienen la base de clientes y el tipo de datos que almacena cada campo
    nombre = models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()