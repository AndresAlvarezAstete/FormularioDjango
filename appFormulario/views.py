from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import EmpleadoForm

# Create your views here.
def show_form(request):
    return render(request, 'registro.html')

def post_form(request):
    nombre = request.POST["nombre"]
    apellidos = request.POST["apellidos"]
    edad = request.POST["edad"]
    direccion = request.POST["direccion"]
    email = request.POST["email"]

    return HttpResponse(f"{nombre} -- {apellidos} -- {edad} -- {direccion} -- {email}")

def show_empleado_form(request):
    form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form':form})

def post_empleado_form(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        edad = form.cleaned_data['edad']
        direccion = form.cleaned_data['direccion']
        email = form.cleaned_data['email']
        return HttpResponse(f"Su nombre es: {nombre} {apellidos}, de edad: {edad}, dirección: {direccion} y su Email es: {email}")