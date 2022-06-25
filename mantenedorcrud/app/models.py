from statistics import mode
from django.db import models

# Create your models here.
class Categoria_videojuego(models.Model):
    nombre_categoria_videojuego = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria_videojuego

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    stock = models.IntegerField(default=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria_videojuego = models.ForeignKey(Categoria_videojuego, on_delete=models.PROTECT, default=1)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre