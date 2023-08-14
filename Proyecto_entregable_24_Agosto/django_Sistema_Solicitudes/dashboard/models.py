from django.db import models

# Create your models here.
class Tickets(models.Model):
    folioTicket =models.CharField("Folio Ticket",max_length=100,default="")
    
    resumen = models.CharField("Resumen",max_length=500,default="")
    archivosAdjuntos = models.BooleanField("Archivos",default=0)
    fechaCreacion = models.DateField("Fecha de creacion",default="")
    direccion = models.CharField("Direccion",max_length=300,default="")
    fechaActualizacion = models.IntegerField("Fecha de modificacion",default=0)
    usuarioEncargado = models.IntegerField("No. de Paginas",default=0)
    fechaAtencion = models.IntegerField("Fecha de modificacion",default=0)
    fechaTerminacionPrevista = models.IntegerField("Fecha de modificacion",default=0)
    fechaTerminacionFinal = models.IntegerField("Fecha de modificacion",default=0)
    statusTicket = models.CharField("Direccion",max_length=2,default="")
    nivelPrioridad = models.CharField("Nivel de prioridad",max_length=50,default="")
    comentariosEncargado = models.CharField("Comentarios",max_length=500,default="")

    def _str_(self):
        return self.folioTicket

class archivos(models.Model):
    folioTicket =  models.CharField("Folio Ticket",max_length=100,default="")
    descricpcionArchivo = models.CharField("Descricpcion Archivo",max_length=500,default="")
    archivos = models.FileField("Archivo",default="")
    fechaArchivo = models.DateField("Fecha de creacion",default="")                  
    def _str_(self):
        return self.folioTicket