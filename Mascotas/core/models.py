from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria



class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=8, verbose_name='Id')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    precio= models.CharField(max_length=20, verbose_name='Precio')
    stock= models.CharField(max_length=20, verbose_name='Stock')

    def __str__(self):
        return self.id
    
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=15, verbose_name='Rut')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    telefono = models.CharField(max_length=15, verbose_name='Telefono')
    direccion= models.CharField(max_length=30, verbose_name='Direccion')
    correo= models.CharField(max_length=30, verbose_name='Correo')

    def __str__(self):
        return self.rut