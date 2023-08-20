from django import forms
from .models import Tickets,archivos

class TicketsForms (forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['resumen','direccion',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['direccion'].widget.attrs.update({'id':'direccionField'})
        

    def clean(self):
        cleaned_data = super().clean()
        resumen = cleaned_data.get('resumen')
        direccion = cleaned_data.get('direccion')   
        

        if not resumen or not direccion:
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data
    def customSave(self):
        data = self.save(commit=False)
        data.save()
        return data
    


class ArchivosForms (forms.ModelForm):
    class Meta:
        model = archivos
        fields = ['idTicket','archivos','fechaCreacion']
    

    def clean(self):
        cleaned_data = super().clean()
        
        folioTicket = cleaned_data.get('idTicket')
        descricpcionArchivo = cleaned_data.get('descricpcionArchivo')
        archivos = cleaned_data.get('archivos')

        if not folioTicket  or not archivos :
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data