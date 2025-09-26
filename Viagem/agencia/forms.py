# agencia/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 

class BootstrapAuthenticationForm(AuthenticationForm):
    """
    Herdamos o formulário de login padrão do Django e adicionamos
    a classe Bootstrap 'form-control' aos campos.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplica a classe 'form-control' ao campo 'username' e 'password'
        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['placeholder'] = self.fields[field_name].label
class BootstrapUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplica a classe 'form-control' aos campos
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            # (Opcional) Adicionar placeholder
            if field_name != 'password2':
                 self.fields[field_name].widget.attrs['placeholder'] = self.fields[field_name].label