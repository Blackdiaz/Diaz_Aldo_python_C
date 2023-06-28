from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

class Index(View):
    template_name = 'index.html'
    def post(self, request):
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexProductos')
        
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        productos = Productos.objects.all()
        form = ProductosForm()
        return render(request, self.template_name, {'form': form,'productos':productos})
    
    def insertar_Producto(request):
        nuevo_Producto = Productos(
            nombre="El gran libro",
            descripcion="Primera edición",
            precio =10.00,
            fecha_registro="2022/02/23",
            status=2022,
        )
        nuevo_Producto.save()
    
        return HttpResponse("Libro insertado correctamente")