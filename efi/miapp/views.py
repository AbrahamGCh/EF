from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Garcia_Persona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def saludo(request):
    return render(request, 'saludo.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        sexo = request.POST['sexo']

        estudiante = Garcia_Persona(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
        )
        estudiante.save()
        messages.success(request, f'Se agregó correctamente la persona {estudiante.nombre}')
        return redirect('estudiantes')  # Redirige a la vista de estudiantes

    return render(request, 'agregar_estudiante.html')

def estudiantes(request):
    estudiantes = Garcia_Persona.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

