from django import forms
from .models import Cliente, Producto

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['id', 'nombre', 'precio', 'stock']

class ClienteForm(forms.ModelForm):

    class Meta:
        model=Cliente
        fields= ['rut', 'nombre', 'telefono', 'direccion','correo']
        