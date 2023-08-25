from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('index', views.index, name = 'index'),
    path('formularios',views.Formulario.as_view(), name='formularios'),
    path('publico',views.Publico.as_view(), name='publico'),
    path('servidor',views.Servidor.as_view(), name='servidor'),
    path('listaTickets',views.ListaTickets.as_view(), name='listaTicketsAll'),
    path('listaTickets/<str:tipoTicket>',views.ListaTickets.as_view(), name='listaTicketsFilter'),
    path('updateTicket/<int:ticketId>/',views.UpdateTicket.as_view(), name='updateTicket'),
    path('estadisticas_tickets',views.estadisticas_tickets,name='estadisticas_tickets'),
    path('descargar_archivo/<int:archivo_id>/', views.descargar_archivo, name='descargar_archivo'),
    #path('formulario',views.Formulario.as_view(), name='formulario'),
    #path('eliminar_libro/<int:libro_id>/',views.EliminarLibro.as_view(), name='eliminar_libro'),
    
]