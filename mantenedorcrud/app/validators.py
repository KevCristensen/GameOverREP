from django.forms import  ValidationError

#function la funcion es más básica, me inyecta lo que escribe el usuario o el archivo, pero no me permite tener un parámetro 
#clase, acá si me permite obtener un parámetro, por ej, el peso máximo sea parametrizable, por ej tener un peso máximo de 10mb
class MaxSizeFileValidator:

    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size * 1048576

        if size > max_size:
            raise ValidationError("El tamaño máximo del archivo debe ser de {self.max_file_size}MB")

        return value