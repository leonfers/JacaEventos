from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render

from core.models import Evento, Atividade, TipoEvento, Tag, Instituicao

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

    class Meta:
        model = Evento
        exclude = {'dono', 'valor', 'gerentes', 'tags_do_evento', 'eventos_satelite'}
        fields = '__all__'


class AdicionarTagEmEventos(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'


class RegistrarAtividades(forms.ModelForm):

    class Meta:
        model = Atividade
        fields = '__all__'


class RegistrarInstituicoes(forms.ModelForm):

    class Meta:
        model = Instituicao
        fields = '__all__'

