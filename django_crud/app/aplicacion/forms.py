#Importamos la dependencia forms
from django import forms
#Importamos el modelo a utilizar
from .models import Contacto

#Creacion de la clase para el Form
class FormContacto(forms.ModelForm):
     class Meta:
          model = Contacto
          #Campos que se van a ocupar del modelo
          fields = {
               'nombre',
               'email',
               'telefono',
          }