from django.urls import path
from . import views

urlpatterns = [
    
    #path('', views.index, name = 'index'),
    path('index', views.Index.as_view(), name = 'indexHome'),
    path('insertar',views.Index.insertar_libro, name='insertar')
]
