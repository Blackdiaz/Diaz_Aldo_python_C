from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect , get_object_or_404
from .models import Archivos,Tickets
from .forms import ArchivosForms,TicketsForms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg, Count
from django.db.models.functions import TruncDate
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#Llamada para el registro del ticket    
class Formulario(View):
    teamplate_name = 'formulario.html'
    
    def post(self,request):
        submitted = False
        if request.method == "POST":
            #se genera una copia del reuqest, para agregar mas datos al reuqest posteriormente
            updated_requestPOST = request.POST.copy()
            updated_requestFILES = request.FILES.copy()

            #Se valida los datos del ticket
            ticketsForms = TicketsForms(request.POST)
            if ticketsForms.is_valid():
                data = ticketsForms.save()
                #Una vez guaardado el ticket, recuperamos el id y lo agregamos al request que se copio anteriormente
                updated_requestPOST.update({'idTicket': data.id})
            else:
                #Imprimimos los errores de los datos de ticket
                print(ticketsForms.errors)
            
            #Validamos si en el ticket contiene un archivos adjunto para continuar
            if len(request.FILES) != 0:
                #Agregamos al request de manera independiente el nombre del archivo
                updated_requestPOST.update({'descricpcionArchivo': request.FILES[u'archivos'].name})
                #Validamos los datos del request para agregar un archivo
                archivosForms = ArchivosForms(updated_requestPOST,updated_requestFILES)
                if archivosForms.is_valid():
                    archivosForms.save()
                    
                else:
                    print(archivosForms.errors)
            

        #Devolvemos los campos llenables a la vista HTML    
        ticketform = TicketsForms()
        archivosform = ArchivosForms()
        messages.error(request, 'Se registro correctamente')
        return render(request, self.teamplate_name,{'ticketform': ticketform,'archivosform': archivosform })
    
    def get(self, request):
        ticketform = TicketsForms()
        archivosform = ArchivosForms()
        return render(request, self.teamplate_name, {'ticketform': ticketform,'archivosform': archivosform })
    

#Llamada para el dashboard que es para el publico
class Publico(View):
    teamplate_name = 'dashboardPublico.html'
    
    
    def get(self, request):
        return render(request, self.teamplate_name)

#LLamada para el dashboard que es para lo servidores publicos
class Servidor(View):
    teamplate_name = 'dashboardServidor.html'
    
    
    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.teamplate_name)

#Llamada para la visualizacion de todos los tickets
class ListaTickets(View):
    teamplate_name = 'listaTickets.html'

    @method_decorator(login_required)
    def get(self, request,tipoTicket=None):
        archivos = Archivos.objects.all()
        # Filtrar los tickets por estado 
        if tipoTicket is not None:
            if tipoTicket!="Cerrado":
                tickets = Tickets.objects.filter(statusTicket=tipoTicket)
            else:
                tickets = Tickets.objects.filter(statusTicket__in=["Completado","cancelado"])
        else:
            tickets = Tickets.objects.all()

        
        return render(request, self.teamplate_name, {'tickets': tickets, 'archivos':archivos})

#Llamada para que un servidor publio actualice los datos de los tickets    
class UpdateTicket(View):
    teamplate_name = 'listaTickets.html'

    @method_decorator(login_required)
    def post(self,request,ticketId):
        
        if request.method == "POST":
            #Obtenemos los datos del ticket por el id
            ticket = get_object_or_404(Tickets,pk=ticketId)

            #Actualizamos los datos del ticket que son editables para el servidor publico
            ticket.nivelPrioridad = request.POST.get('nivelPrioridad')
            ticket.statusTicket = request.POST.get('statusTicket')
            ticket.usuarioEncargado = request.POST.get('usuarioEncargado')
            ticket.comentariosEncargado = request.POST.get('comentariosEncargado')
            ticket.save()
            #Devolvemos los tickets actualizados a la vista HTML
            tickets = Tickets.objects.all()
            
                

        return render(request,self.teamplate_name, {'tickets': tickets})
    
    def get(self, request):
        ticketform = TicketsForms()
        archivosform = ArchivosForms()
        return render(request, self.teamplate_name, {'ticketform': ticketform,'archivosform': archivosform })
    


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

    #Desglosamos el query set en listas para las graficas
    for ticketFecha in promedio_ticket_al_dia:
        sumaDiasTotales += ticketFecha['conteo_dias']
        
    labels_promedio_ticket_al_dia = [registro['dia'].strftime("%d de %B de %Y").replace("'", '"') for registro in promedio_ticket_al_dia]
    data_promedio_ticket_al_dia = [registro['conteo_dias'] for registro in promedio_ticket_al_dia]



    return render(request,'estadisticas.html',{
        'total_tickets':total_tickets,
        'fecha_reciente': fecha_reciente,
        'labels_promedio_ticket_al_dia':labels_promedio_ticket_al_dia,
        'data_promedio_ticket_al_dia':data_promedio_ticket_al_dia,
        'conteoTickets_dia':sumaDiasTotales

    })   

#LLamada para descargar el archivo adunto al ticket
def descargar_archivo(request, archivo_id):
    archivo = get_object_or_404(Archivos, id=archivo_id)
    response = HttpResponse(archivo.archivos, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{archivo.descricpcionArchivo}"'
    return response