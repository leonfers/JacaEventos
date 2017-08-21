from django import forms
from .models import Evento, Tag, TipoEvento, Instituicao, GerenciaEvento, EventoInstituicao, Trilha, Atividade, AtividadeContinua, AtividadeAdministrativa, EventoSatelite, EspacoFisico


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
    nome = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)

    class Meta:
        model = Tag
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


class AdicionarEventosSatelite(forms.ModelForm):

    class Meta:
        model = EventoSatelite
        fields = '__all__'


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
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)

    class Meta:
        model = Atividade
        exclude = ['periodo', 'horario', 'evento']
        fields = '__all__'


class RegistrarAtividadeContinua(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)

    class Meta:
        model = AtividadeContinua
        exclude = ['periodo', 'horario', 'evento']
        fields = '__all__'


class RegistrarAtividadeAdministrativa(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}), required=False)

    class Meta:
        model = AtividadeAdministrativa
        exclude = ['periodo', 'horario', 'evento']
        fields = '__all__'


class RegistrarEspacoFisicoEvento(forms.ModelForm):

    class Meta:
        model = EspacoFisico
        exclude = ['evento']
        fields = '__all__'