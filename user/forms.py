from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render
from django import forms
from core.models import TipoEvento

from core.models import Evento, TipoEvento, Tag, Instituicao, GerenciaEvento, EventoInstituicao,EventoSatelite, Trilha, Atividade, AtividadeAdministrativa, AtividadeContinua

User = get_user_model()


class RegistrarUsuario(forms.ModelForm):

    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirmacao de Senha', widget=forms.PasswordInput)

    def verificar_senha(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("A Confirmacao nao esta Correta")
        return senha2

    def save(self, commit=True):
        user = super(RegistrarUsuario, self).save(commit=False)
        user.set_password(self.cleaned_data['senha1'])

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        # abstract = True
        fields = ['username','email','nome']


class RegistrarEvento(forms.ModelForm):
    nome = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),required=False)
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    tipo_evento = forms.TypedChoiceField(choices=TipoEvento.choices(), coerce=str,required=False)

    class Meta:
        model = Evento
        exclude = {'dono', 'valor', 'gerentes', 'tags_do_evento', 'eventos_satelite'}
        fields = ['nome', 'descricao', 'valor', 'tipo_evento']
        #foram inseridos novos campos dentro do modelo de eventos
        #tu vai ter que colocar no forms de registrar evento um registro de periodo e de endereço como fizemos em atividade antes.



class AdicionarTagEmEventos(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

#
# class RegistrarAtividades(forms.ModelForm):
#     descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}))
#
#     class Meta:
#         model = Atividade
#         exclude = {'trilha', 'evento', 'periodo'}
#         fields = '__all__'
#

class RegistrarInstituicoes(forms.ModelForm):

    class Meta:
        model = Instituicao
        fields = '__all__'


class RegistrarGerentes(forms.ModelForm):

    class Meta:
        model = GerenciaEvento
        exclude = {'evento'}
        fields = '__all__'


# class RegistrarEventosSatelite(forms.ModelForm):
#
#     class Meta:
#         model = EventoSatelite
#         fields = '__all__'


class RegistrarTagEventos(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

class AssociarInstituicoesEvento(forms.ModelForm):

    class Meta:
        model = EventoInstituicao
        exclude = ['evento_relacionado']
        fields = '__all__'


class TrilhaAtividadeEvento(forms.ModelForm):

    class Meta:
        model = Trilha
        fields = '__all__'


class RegistrarAtividade(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = Atividade
        fields = '__all__'

class RegistrarAtividadeContinua(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = AtividadeContinua
        fields = '__all__'

class RegistrarAtividadeAdministrativa(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = AtividadeAdministrativa
        fields = '__all__'


