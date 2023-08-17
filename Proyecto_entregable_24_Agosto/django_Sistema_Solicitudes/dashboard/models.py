from django.db import models

# Create your models here.
class Tickets(models.Model):
    folioTicket = models.CharField("Folio Ticket",max_length=100,default="") 
    resumen = models.CharField("Resumen",max_length=500,default="")
    archivosAdjuntos = models.CharField("Archivos",max_length=2,default=0)
    direccion = models.CharField("Direccion",max_length=300,default="")
    fechaCreacion = models.DateField("Fecha de creacion",default="")
    fechaActualizacion = models.DateField("Fecha de modificacion",default="")
    usuarioEncargado = models.CharField("Usuario encargado",max_length=50,default="")
    fechaAtencion = models.DateField("Fecha de atencion",default="")
    fechaTerminacionPrevista = models.DateField("Fecha de finalizacion programada",default="")
    fechaTerminacionFinal = models.DateField("Fecha de finalizacion real",default="")
    statusTicket = models.CharField("Status ticket",max_length=2,default="")
    nivelPrioridad = models.CharField("Nivel de prioridad",max_length=2,default="")
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

class direcciones(models.Model):
    calle =  models.CharField("Calle",max_length=200,default="")
    colonia = models.CharField("Colonia",max_length=500,default="")
    ciudad = models.CharField("Colonia",max_length=100,default="")                    
    estado = models.CharField("Colonia",max_length=50,default="") 
    cp = models.CharField("Colonia",max_length=8,default="") 
    def _str_(self):
        return self.folioTicket
