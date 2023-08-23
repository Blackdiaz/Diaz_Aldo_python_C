from django.db import models
import datetime

# Create your models here.
class Tickets(models.Model):
    resumen = models.CharField("Resumen",max_length=500,default="")
    descripcion = models.CharField("Descripcion",max_length=1000,default="")
    direccion = models.CharField("Direccion",max_length=300,default="")
    fechaCreacion = models.DateTimeField("Fecha de creacion" ,null=True,default=datetime.datetime.now)
    fechaActualizacion = models.DateTimeField("Fecha de modificacion" ,null=True,default=None)
    usuarioEncargado = models.CharField("Usuario encargado",max_length=50,default="")
    fechaAtencion = models.DateTimeField("Fecha de atencion" ,null=True,default=None)
    fechaTerminacionPrevista = models.DateTimeField("Fecha de finalizacion programada" ,null=True,default=None)
    fechaTerminacionFinal = models.DateTimeField("Fecha de finalizacion real" ,null=True,default=None)
    statusTicket = models.CharField("Status ticket",max_length=2,default="")
    nivelPrioridad = models.CharField("Nivel de prioridad",max_length=2,default="")
    comentariosEncargado = models.CharField("Comentarios",max_length=500,default="")

    def _str_(self):
        return self.pk

class archivos(models.Model):
    idTicket =  models.CharField("Folio Ticket",max_length=100,default="")
    descricpcionArchivo = models.CharField("Descricpcion Archivo",max_length=500,default="")
    archivos = models.FileField("Archivo",upload_to='documents/%Y/%m/%d')
    fechaCreacion = models.DateTimeField("Fecha de creacion",null=True,default=datetime.datetime.now)                  
    def _str_(self):
        return self.pk

