from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

#Create your views here.
def index(request):
    
    return HttpResponse("Hola Mundo")

class Index(View):
    template_name = 'index.html'

    def post():

        return
    
    def get(self,request):
        print("Ya inicio mi Get..")
        return render (request,self.template_name)

    def insertar_libro(request):
        nuevo_libro = Libros(
            titulo="El gran libro",
            edicion="Primera edición",
            editorial="Editorial XYZ",
            año_publicacion=2022,
            paginas=200
        )
        nuevo_libro.save()
    
        return HttpResponse("Libro insertado correctamente")

