from django import forms
from .models import Tickets,direcciones,archivos

class TicketsForms (forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['resumen','direccion','archivosAdjuntos',]
    def clean(self):
        cleaned_data = super().clean()
        folioTicket = cleaned_data.get('folioTicket') 
        resumen = cleaned_data.get('resumen') 
        fechaCreacion = cleaned_data.get('fechaCreacion')
        direccion = cleaned_data.get('direccion') 
        archivosAdjuntos = cleaned_data.get('archivosAdjuntos')     
        fechaActualizacion = cleaned_data.get('fechaActualizacion') 
        usuarioEncargado = cleaned_data.get('usuarioEncargado') 
        fechaAtencion = cleaned_data.get('fechaAtencion') 
        fechaTerminacionPrevista = cleaned_data.get('fechaTerminacionPrevista') 
        fechaTerminacionFinal =cleaned_data.get('fechaTerminacionFinal') 
        statusTicket = cleaned_data.get('statusTicket')
        nivelPrioridad = cleaned_data.get('nivelPrioridad')
        comentariosEncargado = cleaned_data.get('comentariosEncargado')

        if not resumen or not fechaCreacion or not direccion:
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data

class direccionesForms (forms.ModelForm):
    class Meta:
        model = direcciones
        fields = ['calle','colonia','ciudad','estado']

    def clean(self):
        cleaned_data = super().clean()
        calle = cleaned_data.get('calle')
        colonia = cleaned_data.get('colonia')
        ciudad = cleaned_data.get('ciudad')
        estado = cleaned_data.get('estado')

        if not calle or not colonia or not ciudad or not estado :
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data

class archivosForms (forms.ModelForm):
    class Meta:
        model = archivos
        fields = ['folioTicket','descricpcionArchivo','archivos','fechaArchivo']

    def clean(self):
        cleaned_data = super().clean()
        
        folioTicket = cleaned_data.get('folioTicket')
        descricpcionArchivo = cleaned_data.get('descricpcionArchivo')
        archivos = cleaned_data.get('archivos')
        fechaArchivo = cleaned_data.get('fechaArchivo')

        if not folioTicket or not descricpcionArchivo or not archivos or not fechaArchivo:
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data