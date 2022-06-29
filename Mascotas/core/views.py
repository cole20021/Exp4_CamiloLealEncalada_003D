from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Cliente, Producto
from .forms import ProductoForm, ClienteForm

# Create your views here.

def index (request):
    return render (request, 'index.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def ProductosStock(request):
    return render(request, 'ProductosStock.html')

def Feriados(request):
    return render(request, 'Feriados.html')








def mostrarprod(request):
    producto= Producto.objects.all()
    datos={
        'producto': producto
    }
    return render(request, 'mostrarprod.html',datos)


def formproductos(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrarprod')
    else:
        producto_form= ProductoForm()
    return render(request, 'formproductos.html', {'producto_form':producto_form})


def modificarprod(request, id):
    producto = Producto.objects.get(id=id)
    datos ={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrarprod')
    return render(request, 'modificarprod.html', datos)

def eliminarprod(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('mostrarprod')








def mostrarclientes(request):
    cliente= Cliente.objects.all()
    datos={
        'cliente': cliente
    }
    return render(request, 'mostrarclientes.html',datos)


def formclientes(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('mostrarclientes')
    else:
        cliente_form= ClienteForm()
    return render(request, 'formclientes.html', {'cliente_form':cliente_form})


def formproductos(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrarprod')
    else:
        producto_form= ProductoForm()
    return render(request, 'formproductos.html', {'producto_form':producto_form})


 







def modificarclientes(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrarclientes')
    return render(request, 'modificarclientes.html', datos)

def eliminarclientes(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrarclientes')

