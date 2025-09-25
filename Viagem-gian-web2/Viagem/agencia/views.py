from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Viagem
from django.urls import reverse_lazy

# C (Create)
class ViagemCreateView(CreateView):
    model = Viagem
    fields = [
        'titulo', 
        'destino', 
        'data_partida', 
        'data_retorno', 
        'duracao_dias', 
        'preco_base', 
        'vagas_disponiveis', 
        'tipo_transporte', 
        'hospedagem_inclusa', 
        'codigo_pacote', 
        'descricao_detalhada' 
    ]
    template_name = 'agencia/viagem_form.html'



# R (Read - Lista de viagens)
class ViagemListView(ListView):
    model = Viagem
    context_object_name = 'viagens' # Nome da variável no template
    template_name = 'agencia/viagem_list.html'

# R (Read - Detalhe de uma viagem)
class ViagemDetailView(DetailView):
    model = Viagem
    context_object_name = 'viagem' # Nome da variável no template
    template_name = 'agencia/viagem_detail.html'

# U (Update)
class ViagemUpdateView(UpdateView):
    model = Viagem
    fields = [
        'titulo', 
        'destino', 
        'data_partida', 
        'data_retorno', 
        'duracao_dias', 
        'preco_base', 
        'vagas_disponiveis', 
        'tipo_transporte', 
        'hospedagem_inclusa', 
        'codigo_pacote', 
        'descricao_detalhada'
    ]
    template_name = 'agencia/viagem_form.html'


# D (Delete)
class ViagemDeleteView(DeleteView):
    model = Viagem
    template_name = 'agencia/viagem_confirm_delete.html'
    success_url = reverse_lazy('viagem_lista')