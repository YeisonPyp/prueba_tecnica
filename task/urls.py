from django.urls import path
from task import views

urlpatterns = [
    path('persona/', views.persona_list),
    path('persona/<int:pk>/', views.persona_detail),
]