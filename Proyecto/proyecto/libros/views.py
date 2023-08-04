from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect , get_object_or_404
from .models import Libros
from .forms import LibroForms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg
# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

class Index(View):
    teamplate_name = 'index.html'
    
    def post(self, request):
          
        return render(request, self.teamplate_name)
    
    @method_decorator(login_required)
    def get(self, request):
        libros = Libros.objects.all()
        
        return render(request, self.teamplate_name, {'libros': libros})

class Formulario(View):
    teamplate_name = 'formulario.html'
    
    def post(self, request):
        form = LibroForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
        
            
        return render(request, self.teamplate_name, {'form': form})
    
    def get(self, request):
        form = LibroForms()
        return render(request, self.teamplate_name, {'form': form})
    
    
class EliminarLibro(View):
    teamplate_name = 'formulario.html'
    def post(self, request, libro_id):
        
        libro = get_object_or_404(Libros,pk=libro_id)
        libro.delete()
        return redirect('index')
    
def estadisticas_libros(request):
    #Obtener el numero total de paginas de todos los libros
    total_paginas = Libros.objects.aggregate(total_paginas=Sum('paginas'))['total_paginas']

    #Obtener el año maximo de publicacion
    max_anio_publicacion = Libros.objects.aggregate(max_anio_publicacion=Max('anio_de_publicacion'))['max_anio_publicacion']

    #Obtener el numero promedio de paginas de todos los libros
    promedio_paginas = Libros.objects.aggregate(promedio_paginas=Avg('paginas'))['promedio_paginas']

    return render(request,'estadisticas/estadisticas_libros.html',{
        'total_paginas':total_paginas,
        'max_anio_publicacion': max_anio_publicacion,
        'promedio_paginas':promedio_paginas

    })

