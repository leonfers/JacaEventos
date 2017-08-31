from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render
from django import forms
from core.models import TipoEvento

from core.models import Evento, TipoEvento, Tag, Instituicao, GerenciaEvento, EventoInstituicao,EventoSatelite, Trilha, Atividade, AtividadeAdministrativa, AtividadeContinua
from user.models import Inscricao, ItemInscricao, CheckinItemInscricao

User = get_user_model()


class RegistrarUsuarioForm( forms.ModelForm ):

    senha1 = forms.CharField( label='Senha', widget=forms.PasswordInput )
    senha2 = forms.CharField( label='Confirmacao de Senha', widget=forms.PasswordInput )

    def verificar_senha( self ):
        senha1 = self.cleaned_data.get( "senha1" )
        senha2 = self.cleaned_data.get( "senha2" )
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError( "A Confirmacao nao esta Correta" )
        return senha2

    def save( self, commit=True ):
        user = super( RegistrarUsuarioForm, self ).save( commit=False )
        user.set_password( self.cleaned_data['senha1'] )

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        # abstract = True
        fields = ['username','email','nome']

class InscricaoEventoForm( forms.ModelForm ):

    class Meta:
        model = Inscricao
        exclude = ['usuario', 'evento']
        fields = '__all__'

class CheckinItemInscricaoEventoForm( forms.ModelForm ):

    class Meta:
        model = CheckinItemInscricao
        # exclude = ['hora', 'data', 'status']
        fields = '__all__'