from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('index', views.index, name = 'index'),
    path('formulario',views.Formulario.as_view(), name='formulario'),
    #path('formulario',views.Formulario.as_view(), name='formulario'),
    #path('eliminar_libro/<int:libro_id>/',views.EliminarLibro.as_view(), name='eliminar_libro'),
    #path('estadisticas/',views.estadisticas_libros,name='estadisticas_libros')
]