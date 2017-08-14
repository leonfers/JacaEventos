from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render
from django import forms
from core.models import TipoEvento

from core.models import Evento, Atividade, TipoEvento, Tag, Instituicao, GerenciaEvento, EventoInstituicao,EventoSatelite

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
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    tipo_evento = forms.TypedChoiceField(choices=TipoEvento.choices(), coerce=str,required=False)

    class Meta:
        model = Evento
        exclude = {'dono', 'valor', 'gerentes', 'tags_do_evento', 'eventos_satelite','tipo_evento'}
        fields = ['nome','descricao',]



class AdicionarTagEmEventos(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'


class RegistrarAtividades(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = Atividade
        exclude = {'trilha', 'evento', 'periodo'}
        fields = '__all__'


class RegistrarInstituicoes(forms.ModelForm):

    class Meta:
        model = Instituicao
        fields = '__all__'


class RegistrarGerentes(forms.ModelForm):

    class Meta:
        model = GerenciaEvento
        exclude = {'evento'}
        fields = '__all__'

#
# class RegistrarEventosSatelite(forms.ModelForm):
#
#     class Meta:
#         model = EventoSatelite



class RegistrarTagEventos(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

class AssociarInstituicoesEvento(forms.ModelForm):

    class Meta:
        model = EventoInstituicao
        exclude = ['evento_relacionado']
        fields = '__all__'


