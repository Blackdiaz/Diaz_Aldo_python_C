from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Libros
from .forms import LibroForms
# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

class Index(View):
    template_name = 'index.html'
    def post(self, request):
        form = LibroForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexLibros')
        
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        libros = Libros.objects.all()
        form = LibroForms()
        return render(request, self.template_name, {'form': form,'libros':libros})
    
    def insertar_libro(request):
        nuevo_libro = Libros(
            titulo="El gran libro",
            edicion="Primera edición",
            editorial="Editorial XYZ",
            anio_de_publicacion=2022,
            paginas=200
        )
        nuevo_libro.save()
    
        return HttpResponse("Libro insertado correctamente")