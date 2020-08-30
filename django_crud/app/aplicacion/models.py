from django.db import models

class Contacto(models.Model):
		id = models.AutoField(primary_key = True)
		nombre = models.CharField(max_length = 200)
		email = models.CharField(max_length = 100)
		telefono = models.CharField(max_length = 8)