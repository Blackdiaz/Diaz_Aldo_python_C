from django.db import models

# Create your models here.
class Tickets(models.Model):
    folioTicket = models.CharField("Folio Ticket",max_length=50,default="") 
    resumen = models.CharField("Resumen",max_length=500,default="")
    archivosAdjuntos = models.CharField("Archivos",max_length=2,default="")
    direccion = models.CharField("Direccion",max_length=300,default="")
    fechaCreacion = models.DateTimeField("Fecha de creacion" ,null=True,default=None)
    fechaActualizacion = models.DateTimeField("Fecha de modificacion" ,null=True,default=None)
    usuarioEncargado = models.CharField("Usuario encargado",max_length=50,default="")
    fechaAtencion = models.DateTimeField("Fecha de atencion" ,null=True,default=None)
    fechaTerminacionPrevista = models.DateTimeField("Fecha de finalizacion programada" ,null=True,default=None)
    fechaTerminacionFinal = models.DateTimeField("Fecha de finalizacion real" ,null=True,default=None)
    statusTicket = models.CharField("Status ticket",max_length=2,default="")
    nivelPrioridad = models.CharField("Nivel de prioridad",max_length=2,default="")
    comentariosEncargado = models.CharField("Comentarios",max_length=500,default="")

    def _str_(self):
        return self.folioTicket

class archivos(models.Model):
    folioTicket =  models.CharField("Folio Ticket",max_length=100,default="")
    descricpcionArchivo = models.CharField("Descricpcion Archivo",max_length=500,default="")
    archivos = models.FileField("Archivo",default="")
    fechaArchivo = models.DateTimeField("Fecha de creacion",null=True,default=None)                  
    def _str_(self):
        return self.folioTicket

class direcciones(models.Model):
    calle =  models.CharField("Calle",max_length=200,default="")
    colonia = models.CharField("Colonia",max_length=500,default="")
    ciudad = models.CharField("Colonia",max_length=100,default="")                    
    estado = models.CharField("Colonia",max_length=50,default="") 
    cp = models.CharField("Colonia",max_length=8,default="") 
    def _str_(self):
        return self.cp
