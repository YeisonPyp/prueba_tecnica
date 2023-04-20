from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from task import views


urlpatterns = [
    path('persona/', views.PersonaList.as_view()),
    path('persona/<int:id>/', views.PersonaDetail.as_view()),
    path('tarea/', views.TareaList.as_view()),
    path('tarea/<int:id>/', views.TareaDetail.as_view()),
    path('persona/f/', views.PersonaFiltros.as_view()),
    path('tarea_filtro_fecha/', views.TareasFiltroFecha.as_view()),
    path('tarea_filtro_persona/', views.TareaFiltroPersona.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)