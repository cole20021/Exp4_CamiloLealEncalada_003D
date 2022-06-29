from django.urls import path
from .views import index,quienessomos,ProductosStock, mostrarprod, formproductos, Feriados,modificarprod,eliminarprod,mostrarclientes,formclientes,modificarclientes,eliminarclientes
urlpatterns=[
    path('', index,name="index"),
    path('ProductosStock/', ProductosStock, name="ProductosStock"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('Feriados', Feriados, name="Feriados"),
    path('mostrarprod/', mostrarprod, name="mostrarprod"),
    path('formproductos/' , formproductos, name="formproductos"),
    path('modificarprod/<id>' , modificarprod, name="modificarprod"),
    path('eliminarprod/<id>' , eliminarprod, name="eliminarprod"),
    path('mostrarclientes', mostrarclientes, name="mostrarclientes",),
    path('formclientes/' , formclientes, name="formclientes"),
    path('modificarclientes/<id>' , modificarclientes, name="modificarclientes"),
    path('eliminarclientes/<id>' , eliminarclientes, name="eliminarclientes"),
    
    
    
]