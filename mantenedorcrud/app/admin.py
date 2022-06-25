from itertools import product
from django.contrib import admin
from . models import Marca, Producto, Contacto, Categoria_videojuego
from .forms import ProductoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca", "categoria_videojuego"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 5
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Categoria_videojuego)