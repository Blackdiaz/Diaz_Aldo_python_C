from django.contrib import admin

from .models import archivos,direcciones,Tickets

admin.site.register(archivos)
admin.site.register(direcciones)
admin.site.register(Tickets)