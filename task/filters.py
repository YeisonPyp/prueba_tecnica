from django_filters import rest_framework as filters
from .models import Persona, Tarea


class TareaFilter(filters.FilterSet):

    fecha_min = filters.DateFilter(field_name='fechalimite', lookup_expr='gte', label='fecha_min')

    fecha_max = filters.DateFilter(field_name='fechalimite', lookup_expr='lte', label='fecha_max')
    fecha = filters.DateFromToRangeFilter(field_name='fechalimite')

    class Meta:
        model = Tarea
        fields = ['fechalimite']