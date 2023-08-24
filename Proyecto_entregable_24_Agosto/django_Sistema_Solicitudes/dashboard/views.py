from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect , get_object_or_404
from .models import archivos,Tickets
from .forms import ArchivosForms,TicketsForms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg, Count
from django.db.models.functions import TruncDate
from django.contrib import messages


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
            #print(request.POST,request.FILES)
            updated_requestPOST = request.POST.copy()
            updated_requestFILES = request.FILES.copy()

            ticketsForms = TicketsForms(request.POST)
            if ticketsForms.is_valid():
                data = ticketsForms.save()
                updated_requestPOST.update({'idTicket': [data.id]})
            else:
                print(ticketsForms.errors)
            if len(request.FILES) != 0:
                updated_requestPOST.update({'descricpcionArchivo': [request.FILES[u'archivos'].name]})
                print("updated",updated_requestPOST)
                archivosForms = ArchivosForms(updated_requestPOST,updated_requestFILES)
                if archivosForms.is_valid():
                    archivosForms.save()
                    
                else:
                    print(archivosForms.errors)
            #TicketsObject = get_object_or_404(Tickets, =account_number)
            #account.current_balance = account.current_balance + amount
            #account.save()

            
        ticketform = TicketsForms()
        archivosform = ArchivosForms()
        messages.error(request, 'Se registro correctamente')
        return render(request, self.teamplate_name,{'ticketform': ticketform,'archivosform': archivosform })
    
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

    @method_decorator(login_required)
    def get(self, request):
        tickets = Tickets.objects.all()
        
        return render(request, self.teamplate_name, {'tickets': tickets})
    
class UpdateTicket(View):
    teamplate_name = 'listaTickets.html'

    @method_decorator(login_required)
    def post(self,request):
        
        if request.method == "POST":
            
            ticket = get_object_or_404(Tickets,pk=request.POST.get('id'))
            print(ticket.resumen)
            ticket.resumen = request.POST.get('resumen')
            ticket.save()
            print(ticket.resumen)
            tickets = Tickets.objects.all()
            
                

        return render(request,self.teamplate_name, {'tickets': tickets})
    


def estadisticas_tickets(request):
    #Obtener el numero total de tickets
    total_tickets = Tickets.objects.aggregate(total_tickets=Count('id'))['total_tickets']
    
    #Obtener la fecha mas reciente de ticket
    fecha_reciente = Tickets.objects.aggregate(fecha_reciente=TruncDate(Max('fechaCreacion')))['fecha_reciente']
    
    #Obtener el numero promedio de tickets al dia
    promedio_ticket_al_dia = Tickets.objects.annotate(
                                    dia=TruncDate('fechaCreacion')
                                ).values('dia').annotate(
                                    conteo_dias=Count('dia')
                                ).order_by('dia')
    sumaDiasTotales = 0
    print(promedio_ticket_al_dia)
    for ticketFecha in promedio_ticket_al_dia:
        sumaDiasTotales += ticketFecha['conteo_dias']
        
    labels_promedio_ticket_al_dia = [registro['dia'].strftime("%d de %B de %Y").replace("'", '"') for registro in promedio_ticket_al_dia]
    data_promedio_ticket_al_dia = [registro['conteo_dias'] for registro in promedio_ticket_al_dia]

    print(labels_promedio_ticket_al_dia)
    print(data_promedio_ticket_al_dia)

    return render(request,'estadisticas.html',{
        'total_tickets':total_tickets,
        'fecha_reciente': fecha_reciente,
        'labels_promedio_ticket_al_dia':labels_promedio_ticket_al_dia,
        'data_promedio_ticket_al_dia':data_promedio_ticket_al_dia,
        'conteoTickets_dia':sumaDiasTotales

    })   