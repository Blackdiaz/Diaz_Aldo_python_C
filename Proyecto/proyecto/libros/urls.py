from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('index', views.Inicio.as_view(), name = 'indexLibros'),
    #path('insertar',views.Inicio.insertar_libro, name='insertar'),
    path('formulario',views.Formulario.as_view(), name='formulario')
]