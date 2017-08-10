from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render
from .models import Periodo, Endereco
from django.contrib.admin import widgets
from datetime import date

class PeriodoForm(forms.ModelForm):
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}),required=False)
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)

    class Meta:
        model = Periodo
        fields = ('data_inicio','data_fim',)

class EnderecoForm(forms.ModelForm):
    pais = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    estado = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    cidade = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    logradouro = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    numero = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)
    cep = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)


    class Meta:
        model = Endereco
        fields = '__all__'