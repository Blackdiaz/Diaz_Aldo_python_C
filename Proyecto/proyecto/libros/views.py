from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Libros
from .forms import LibroForms
# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

class Inicio(View):
    teamplate_name = 'index.html'
    
    def post(self, request):
          
        return render(request, self.teamplate_name)
    
    def get(self, request):
        libros = Libros.objects.all()
        
        return render(request, self.teamplate_name, {'libros': libros})

class Formulario(View):
    teamplate_name = 'formulario.html'
    
    def post(self, request):
        form = LibroForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inicio')
        
            
        return render(request, self.teamplate_name, {'form': form})
    
    def get(self, request):
        form = LibroForms()
        return render(request, self.teamplate_name, {'form': form})