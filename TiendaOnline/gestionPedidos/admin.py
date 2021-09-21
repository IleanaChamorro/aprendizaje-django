from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

#Definir que campos quiero ver
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
#Busqueda de registros  
    search_fields=("nombre", "telefono")


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)

