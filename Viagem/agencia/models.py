from django.db import models
from django.urls import reverse
# Create your models here.
class Viagem(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título da Viagem")
    destino = models.CharField(max_length=100)
    
    data_partida = models.DateField(verbose_name="Data de Partida")
    data_retorno = models.DateField(verbose_name="Data de Retorno")
    duracao_dias = models.IntegerField(verbose_name="Duração (dias)")
    
    
    preco_base = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Base (R$)")
    vagas_disponiveis = models.PositiveIntegerField(default=10, verbose_name="Vagas Disponíveis")
    
    
    tipo_transporte = models.CharField(
        max_length=50, 
        choices=[('AEREO', 'Aéreo'), ('TERRESTRE', 'Terrestre'), ('MARITIMO', 'Marítimo')],
        verbose_name="Tipo de Transporte"
    )
    hospedagem_inclusa = models.BooleanField(default=True, verbose_name="Hospedagem Inclusa")
    
    
    codigo_pacote = models.CharField(max_length=20, unique=True, verbose_name="Código do Pacote")
    descricao_detalhada = models.TextField(verbose_name="Descrição Completa")

    def __str__(self):
        return f'{self.titulo} para {self.destino}'

    def get_absolute_url(self):
        return reverse('viagem_detalhe', kwargs={'pk': self.pk})