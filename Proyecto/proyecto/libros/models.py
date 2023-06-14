from django.db import models

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField("Titulo",max_length=300,default="")
    edicion = models.CharField("Edicion",max_length=300,default="")
    editorial = models.CharField("Editorial",max_length=300,default="")
    anio_de_publicacion = models.IntegerField("Año de publicacion",default=0)
    pagina = models.IntegerField("No. de Paginas",default=0)
    
    def _str_(self):
        return self.titulo