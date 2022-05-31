from pickletools import read_long1
from unittest.util import _MAX_LENGTH
from urllib import request

from pkg_resources import require
from .models import Marca, Producto, Marca
from rest_framework import serializers

#Otra manera para ver en nuestra api el nombre de la marca

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    #De esta manera podemos ver en nuestra api el nombre de la marca
    nomber_marca = serializers.CharField(read_only = True, source = "marca.nombre")
    #
    #
    marca = MarcaSerializer(read_only = True)
    #De esta manera podemos ver más ordenado nuestra API

    #Ahora recuperaremos nuestro cambo de combobox en donde salen todas las marcas
    marca_id = serializers.PrimaryKeyRelatedField(queryset = Marca.objects.all(), source = "marca")
    #
    #Crearé una validación personalizada 
    nombre = serializers.CharField(required = True, min_length = 2)

    #Más personalizado, una validación si es que el nombre ya existe (No importa si presenta diferencias en caracteres capitalizados)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact = value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")

        return value


    class Meta:
        model = Producto
        fields = '__all__'