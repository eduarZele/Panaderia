from django.shortcuts import redirect, render
from django.db import connection
from .models import Clientes

# Create your views here.

TEMPLATE_DIR =  (
    'os.path.join(BASE_DIR, "templates")'
)
def layout(request):
    return render(request, 'layout.html')

# Views de Clientes
def agregar(request):
    
    return render(request, 'Clientes/agregar.html')

def listar(request):
    
    with connection.cursor() as cursor:
        cursor.execute("EXEC prueba")  # Llama al procedimiento almacenado
        clientes = cursor.fetchall()  # Obtén los resultados si es necesario
        #print(clientes)
        
    return render(request, 'Clientes/listar.html' , {'Clientes': clientes})


def agregar(request):
    if request.method == 'POST':
        if (request.POST.get('name') and 
            request.POST.get('apellido') and 
            request.POST.get('telefono')):
                """cliente = Clientes()
                cliente.nombre = request.POST.get('name')
                cliente.apellido = request.POST.get('apellido')
                cliente.telefono = request.POST.get('telefono')"""
                nombre = request.POST.get('name')
                apellido = request.POST.get('apellido')
                telefono = request.POST.get('telefono')
                
                try: 
                    with connection.cursor() as cursor:
                        cursor.execute("EXEC agregar @nombre=%s, @apellido=%s, @telefono=%s", [nombre, apellido, telefono])
                    #cliente.save()
                    return redirect('listar')
                except:
                    return render(request, 'Clientes/agregar.html', {'error_message': 'Asegurate de Ingresar campos correctos'})
    else:
        return render(request, 'Clientes/agregar.html')
    
    
def actualizar(request, id):
    try:
        if request.method == 'POST':
            if (request.POST.get('name') and 
                request.POST.get('apellido') and 
                request.POST.get('telefono')):
                    nombre = request.POST.get('name')
                    apellido = request.POST.get('apellido')
                    telefono = request.POST.get('telefono')
                    id = request.POST.get('Id')
                    try: 
                        with connection.cursor() as cursor:
                            cursor.execute("EXEC actualizar @id=%s, @nombre=%s, @apellido=%s, @telefono=%s", [id, nombre, apellido, telefono])
                        return redirect('listar')
                    except:
                        cliente = Clientes.objects.get(pk = id)
                        clientes = Clientes.objects.all()
                        datos = {'clientes': clientes, 'clienteU': cliente}
                        return render(request, 'Clientes/actualizar.html', datos)
        else:
            cliente = Clientes.objects.get(pk = id)
            clientes = Clientes.objects.all()
            datos = {'clientes': clientes, 'clienteU': cliente}
            return render(request, 'Clientes/actualizar.html', datos)
            
            
    except Clientes.DoesNotExist:
            cliente = Clientes.objects.get(pk = id)
            clientes = Clientes.objects.all()
            datos = {'clientes': clientes, 'clienteU': cliente}
            return render(request, 'Clientes/actualizar.html', datos)
        
    
    return render(request, 'Clientes/actualizar.html')
    
def eliminar(request, id):
    try:
        if request.method == 'POST':
            if request.POST.get('id'):
                id = request.POST.get('id')
                try:
                    with connection.cursor() as cursor:
                        cursor.execute("EXEC eliminar @id=%s", [id])
                        return redirect('listar')
                
                except:
                    clientes = Clientes.objects.all()
                    cliente = Clientes.objects.get(pk = id)
                    datos = {'clientes': clientes, 'clienteU': cliente}
                    return render(request, 'Clientes/eliminar.html', datos)
                    
        else:
            clientes = Clientes.objects.all()
            cliente = Clientes.objects.get(pk = id)
            datos = {'clientes': clientes, 'clienteU': cliente}
            return render(request, 'Clientes/eliminar.html', datos)
        
    except Clientes.DoesNotExist:
        clientes = Clientes.objects.all()
        cliente = None
        datos = {'clientes': clientes, 'clienteU': cliente}
        return render(request, 'Clientes/eliminar.html', datos)    