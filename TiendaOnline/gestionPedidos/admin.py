from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

#Definir que campos quiero ver
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
#Busqueda de registros  
    search_fields=("nombre", "telefono")

#Filtro de busqueda por seccion
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

#Filtro por fecha
class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)

