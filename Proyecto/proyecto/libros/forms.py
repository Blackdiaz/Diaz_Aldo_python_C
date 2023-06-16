from django import forms
from .models import Libros

class LibroForms (forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo','edicion','editorial','anio_de_publicacion','paginas']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        edicion = cleaned_data.get('edicion')
        editorial = cleaned_data.get('editorial')
        anio_publicacion = cleaned_data.get('anio_publicacion')
        paginas = cleaned_data.get('paginas')

        if not titulo or not edicion or not editorial or not anio_publicacion or not paginas:
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data