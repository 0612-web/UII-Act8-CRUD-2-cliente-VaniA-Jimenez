from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_cliente/listar_cliente.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST.get('direccion', '')
        telefono = request.POST['telefono']
        email = request.POST.get('email', '')
        
        Cliente.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email
        )
        return redirect('inicio')
    return render(request, 'app_cliente/agregar_cliente.html')

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.direccion = request.POST.get('direccion', '')
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST.get('email', '')
        cliente.save()
        return redirect('inicio')
    return render(request, 'app_cliente/editar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('inicio')
    return render(request, 'app_cliente/borrar_cliente.html', {'cliente': cliente})