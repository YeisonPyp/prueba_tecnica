from .models import Persona
from rest_framework import viewsets, permissions
from .serializers import PersonaSerializer


class PersonaViewSet (viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer