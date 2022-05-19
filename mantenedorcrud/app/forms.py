from tkinter import Widget
from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        # si queremos que tenga el orden del modelo y traiga todo, se debe ejecutar esta instruccion, asi no ejecutamos 1 por 1

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        
        widgets = {
            "fecha_fabricacion" : forms.SelectDateWidget()
        }