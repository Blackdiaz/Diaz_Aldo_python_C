from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include("libros.urls")),
    path('login/',views.custom_login ,name='login'),
    path('logout/', views.custom_logout ,name='logout'),
    
]