from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField("Nombre",max_length=300,default="")
    descripcion = models.CharField("Descripcion",max_length=300,default="")
    precio = models.DecimalField("Precio",decimal_places=2,max_digits=10,default=0)
    fecha_registro = models.CharField("Fecha de registro",max_length=300,default="")
    estatus = models.BooleanField("Estatus",default=False)
    
    def _str_(self):
        return self.nombre