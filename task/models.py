from django.db import models

class Persona(models.Model):

    documento = models.CharField(max_length=15)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    celular = models.CharField(max_length=15)
    fechanacimiento = models.DateTimeField()
    