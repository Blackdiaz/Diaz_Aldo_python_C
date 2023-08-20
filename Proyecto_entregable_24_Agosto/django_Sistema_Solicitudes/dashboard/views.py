from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect , get_object_or_404
from .models import archivos,Tickets
from .forms import ArchivosForms,TicketsForms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    
class Formulario(View):
    teamplate_name = 'formulario.html'
    
    def post(self,request):
        submitted = False
        if request.method == "POST":
            #resumen = request.POST.get('resumen')
            ##direccion = request.POST.get('direccion')
            #archivosAdjuntos = request.POST.get('archivosAdjuntos')
            print(request.POST,request.FILES)
            updated_request = request.POST.copy()
            ticketsForms = TicketsForms(request.POST)
            if ticketsForms.is_valid():
                data = ticketsForms.save()
                updated_request.update({'idTicket': [data.id]})
            archivosForms = ArchivosForms(updated_request)
            if archivosForms.is_valid():
                archivosForms.save()
            else:
                print("No es valido")
            #TicketsObject = get_object_or_404(Tickets, =account_number)
            #account.current_balance = account.current_balance + amount
            #account.save()

            
        
            
        return render(request, self.teamplate_name)
    
    def get(self, request):
        ticketform = TicketsForms()
        archivosform = ArchivosForms()
        return render(request, self.teamplate_name, {'ticketform': ticketform,'archivosform': archivosform })
    


class Publico(View):
    teamplate_name = 'dashboardPublico.html'
    
    
    def get(self, request):
        return render(request, self.teamplate_name)

class Servidor(View):
    teamplate_name = 'dashboardServidor.html'
    
    
    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.teamplate_name)

class ListaTickets(View):
    teamplate_name = 'listaTickets.html'
    
    def update_ticket(self,request):
        
        if request.method == "POST":
            
            ticket = Tickets.objects.get(id=request.POST.get('id'))
            print(ticket)
            ticketform = TicketsForms(request.POST,instance=ticket)
            if ticketform.is_valid():
                ticketform.save()
                tickets = Tickets.objects.all()

        return render(request, self.teamplate_name, {'tickets': tickets})

    def ticket_view(request, id):
        incident = get_object_or_404(id=id)
        short_description = incident.short_description
        return render(request, "detailTicket.html", locals())

    @method_decorator(login_required)
    def get(self, request):
        tickets = Tickets.objects.all()
        
        return render(request, self.teamplate_name, {'tickets': tickets})