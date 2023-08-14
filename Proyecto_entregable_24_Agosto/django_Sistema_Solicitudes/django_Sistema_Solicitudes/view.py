from django.http import HttpResponse
from django.shortcuts import redirect,render, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('/libros/inicio')

def custom_login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('----> SI, entro')
            return redirect('/dashboard/servidor')
        else:
            print('----> No, entro')
            messages.error(request, 'Credenciales invalidas')
            return redirect('/dashboard/publico')

    return render(request,template_name)


