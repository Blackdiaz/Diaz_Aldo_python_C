from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect , get_object_or_404
from .models import archivos,direcciones,Tickets
from .forms import archivosForms,direccionesForms,TicketsForms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Formulario(View):
    teamplate_name = 'formulario.html'
    
    def post(self, request):
        form = TicketsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
        
            
        return render(request, self.teamplate_name, {'form': form})
    
    def get(self, request):
        form = TicketsForms()
        return render(request, self.teamplate_name, {'form': form})