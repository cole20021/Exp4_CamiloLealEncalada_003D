# Generated by Django 4.0.5 on 2022-06-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('correo', models.CharField(max_length=30, verbose_name='Correo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('precio', models.CharField(max_length=20, verbose_name='Precio')),
                ('stock', models.CharField(max_length=20, verbose_name='Stock')),
            ],
        ),
    ]
