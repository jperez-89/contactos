from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import FormContacto
from django.core.exceptions import ObjectDoesNotExist

def Home(request):
     lstContactos = Contacto.objects.all()
     context = {'lstContactos': lstContactos}
     return render(request, 'index.html', context)

# Vista para agregar contacto
def agregarContacto(request):
     if request.method == 'POST':
          form = FormContacto(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, 'Datos almacenados correctamente')
          else:
               messages.error(request, 'Se presentó un problema con los datos')
          return redirect('index')
     else:
          form = FormContacto()
     return render(request, 'agregarContacto.html', {'form': form})

# def listarContactos(request):
#      lstContactos = Contactos.objects.all()
#      context = {'lstContactos': lstContactos}
#      return render(request, 'aplicacion/listarContactos.html', context)

def editarContacto(request, id):
     #Se definen las variables con None para que den error al ejecutar la vista
     form = None
     error = None
     
     try:
          # Cuando solicitamos la informacion a la base de datos del contacto que vamos a editar
          contacto = Contacto.objects.get(id=id)
          if request.method == 'GET':               
               form = FormContacto(instance=contacto)
          else:
               # Cuando damo en el boton de guardar lo que hemos editado
               form = FormContacto(request.POST, instance=contacto)
               if form.is_valid():
                    form.save()
                    messages.success(request, 'Datos actualizados correctamente')
               else:
                    messages.error(request, 'Se presentó un problema con los datos')
               return redirect('index')
          
     except ObjectDoesNotExist as e:
          error = e
          
     #Cuando se aplica el GET redirecciona al form con los datos, si no encuentra el id enviar el error
     return render(request, 'agregarContacto.html', {'form': form, 'error': error})

def eliminarContacto(request, id):
     #Se definen las variables con None para que den error al ejecutar la vista
     form = None
     error = None
     
     try:
          #Opcion 1 Eliminacion directa
          #Obtenemos el contacto por medio del id y lo eliminamos
          contacto = Contacto.objects.get(id=id)
          if contacto.delete():
               messages.success(request, 'Dato eliminado correctamente')
          else:
               messages.error(request, 'Se presentó un problema con los datos')
          
          return redirect('index')

          #Opcion 2 Eliminacion logica
          # Debemos tener un campo, por ejemplo de Estado en la tabla que sea true o false
          #contacto = Contacto.objects.get(id=id)
          #contacto.estado = False
          #contacto.save()
          #return redirect('index')
     
     except ObjectDoesNotExist as e:
          error = e