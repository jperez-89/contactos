from django.urls import path
from .views import *

urlpatterns = [
     path('', Home, name = 'index'),
     path('agregarContacto/', agregarContacto, name = 'agregarContacto'),
     path('editarContacto/<int:id>', editarContacto, name = 'editarContacto'),
     path('eliminarContacto/<int:id>', eliminarContacto, name = 'eliminarContacto'),
]