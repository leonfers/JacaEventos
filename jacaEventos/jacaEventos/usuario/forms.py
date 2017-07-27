from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render

class RegistrarUsuario(forms.Form):

    User = get_user_model()

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
        user.set_senha(self.cleaned_data['senha'])

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        campos = ['username', 'email']


