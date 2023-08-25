from django import forms
from .models import Tickets,Archivos

class TicketsForms (forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Tickets
        fields = ['resumen','descripcion','direccion',]
       

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['direccion'].widget.attrs.update({'id':'direccionField'})
        
        

    def clean(self):
        cleaned_data = super().clean()
        resumen = cleaned_data.get('resumen')
        descripcion = cleaned_data.get('descripcion') 
        direccion = cleaned_data.get('direccion')   
        

        if not resumen or not direccion:
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data




class ArchivosForms (forms.ModelForm):
    archivos =forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    class Meta:
        model = Archivos
        fields = ['idTicket','descricpcionArchivo','archivos']
        
    

    def clean(self):
        cleaned_data = super().clean()
        idTicket = cleaned_data.get('idTicket')
        descricpcionArchivo = cleaned_data.get('descricpcionArchivo')
        archivos = cleaned_data.get('archivos')
        print("clean",cleaned_data)
        if not descricpcionArchivo or not archivos :
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data