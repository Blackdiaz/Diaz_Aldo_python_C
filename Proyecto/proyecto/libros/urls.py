from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('index', views.Index.as_view(), name = 'index'),
    #path('insertar',views.Inicio.insertar_libro, name='insertar'),
    path('formulario',views.Formulario.as_view(), name='formulario'),
    path('eliminar_libro/<int:libro_id>/',views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('estadisticas/',views.estadisticas_libros,name='estadisticas_libros')
]