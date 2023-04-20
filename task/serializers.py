from rest_framework import serializers
from .models import Persona, Tarea

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('id', 'documento', 'nombre', 'apellido', 'celular', 'fechanacimiento')


class TareaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarea
        fields = ('id', 'persona', 'titulo', 'descripcion','fechalimite')