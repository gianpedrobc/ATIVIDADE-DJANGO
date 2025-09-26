# agencia/urls.py

from django.urls import path
from .views import (
    # Importe TODAS as views do seu arquivo views.py
    ViagemListView, 
    ViagemDetailView, 
    ViagemCreateView, 
    ViagemUpdateView, 
    ViagemDeleteView
)

urlpatterns = [
    # Mapeia rotas INDIVIDUAIS, usando .as_view() e NÃO o include()
    
    # READ (Lista): /
    path('', ViagemListView.as_view(), name='viagem_lista'), 
    
    # CREATE: /nova/
    path('nova/', ViagemCreateView.as_view(), name='viagem_nova'), 
    
    # READ (Detalhe): /1/
    path('<int:pk>/', ViagemDetailView.as_view(), name='viagem_detalhe'), 
    
    # UPDATE: /1/editar/
    path('<int:pk>/editar/', ViagemUpdateView.as_view(), name='viagem_editar'), 
    
    # DELETE: /1/excluir/
    path('<int:pk>/excluir/', ViagemDeleteView.as_view(), name='viagem_excluir'),
]