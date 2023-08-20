from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('index', views.index, name = 'index'),
    path('formularios',views.Formulario.as_view(), name='formulario'),
    path('publico',views.Publico.as_view(), name='publico'),
    path('servidor',views.Servidor.as_view(), name='servidor'),
    path('listaTickets',views.ListaTickets.as_view(), name='listaTickets'),
    path('updateTicket',views.ListaTickets.update_ticket, name='updateTicket'),
    path('ticket_view/<str:id>/',views.ListaTickets.ticket_view, name='ticket_view'),
    #path('formulario',views.Formulario.as_view(), name='formulario'),
    #path('eliminar_libro/<int:libro_id>/',views.EliminarLibro.as_view(), name='eliminar_libro'),
    #path('estadisticas/',views.estadisticas_libros,name='estadisticas_libros')
]