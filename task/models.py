from django.db import models

class Persona(models.Model):

    documento = models.CharField(max_length=15)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    celular = models.CharField(max_length=15)
    fechanacimiento = models.DateField()
    

class Tarea(models.Model):

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechalimite = models.DateField()
    
