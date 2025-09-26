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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm 

# C (Create)
class ViagemCreateView(LoginRequiredMixin, CreateView):
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

class ViagemUpdateView(LoginRequiredMixin, UpdateView):
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

class ViagemDeleteView(LoginRequiredMixin, DeleteView):
    model = Viagem
    template_name = 'agencia/viagem_confirm_delete.html'
    success_url = reverse_lazy('viagem_lista')

class CadastroUsuarioView(CreateView):
    # Usa o formulário de criação de usuário padrão do Django
    form_class = UserCreationForm
    
    template_name = 'registration/cadastro.html' 
    success_url = reverse_lazy('login') 