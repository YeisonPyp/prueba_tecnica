from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Persona, Tarea
from .serializers import PersonaSerializer, TareaSerializer



class PersonaList(APIView):
   
    def get(self, request, format=None):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonaDetail(APIView):
    
    def get_object(self, id):
        try:
            return Persona.objects.get(id=id)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        persona = self.get_object(id)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        persona = self.get_object(id)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        persona = self.get_object(id)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PersonaFiltros(generics.ListAPIView):

    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['documento']


'''def persona_filtro(request):
    f = PersonaFilter(request.GET, queryset=Persona.objects.all())
    return render(request, 'my_app/template.html', {'filter': f})
    
'''

class TareaList(APIView):
   
    def get(self, request, format=None):
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TareaDetail(APIView):
    
    def get_object(self, id):
        try:
            return Tarea.objects.get(id=id)
        except Tarea.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        tarea = self.get_object(id)
        serializer = TareaSerializer(tarea)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        tarea = self.get_object(id)
        serializer = TareaSerializer(tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        tarea = self.get_object(id)
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

