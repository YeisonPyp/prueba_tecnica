from django_filters import rest_framework as filters
from .models import Persona, Tarea


class PersonaFilter(filters.FilterSet):

    documentop = filters.CharFilter(method='documento_filter')

    class Meta:
        model = Persona
        fields = ['documento']

    def documento_filter(self, queryset, documento, value):
        return queryset.filter(**{
            documento: value,
        })