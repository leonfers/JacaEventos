from django import forms

from user.models import Inscricao
from .models import Evento, Tag, TipoEvento, Instituicao, GerenciaEvento, EventoInstituicao, Trilha, AtividadePadrao, \
    AtividadeContinua, AtividadeAdministrativa, EventoSatelite, EspacoFisico


class RegistrarEventoForm(forms.ModelForm):
    nome = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                           required=False)
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                required=False)
    tipo_evento = forms.TypedChoiceField(choices=TipoEvento.choices(), coerce=str, required=False)

    class Meta:
        model = Evento
        exclude = {'dono', 'valor', 'gerentes', 'tags_do_evento', 'eventos_satelite'}
        fields = ['nome', 'descricao', 'valor', 'tipo_evento']


class AdicionarTagEmEventosForm(forms.ModelForm):
    nome = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                           required=False)

    class Meta:
        model = Tag
        fields = '__all__'


class RegistrarInstituicoesForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'


class RegistrarGerentesForm(forms.ModelForm):
    class Meta:
        model = GerenciaEvento
        exclude = {'evento'}
        fields = '__all__'


class AdicionarEventosSateliteForm(forms.ModelForm):
    class Meta:
        model = EventoSatelite
        fields = '__all__'


class RegistrarTagEventosForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class AssociarInstituicoesEventoForm(forms.ModelForm):
    class Meta:
        model = EventoInstituicao
        exclude = ['evento_relacionado']
        fields = '__all__'


class TrilhaAtividadeEventoForm(forms.ModelForm):
    class Meta:
        model = Trilha
        fields = '__all__'


class RegistrarAtividadeForm(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                required=False)

    class Meta:
        model = AtividadePadrao
        exclude = ['periodo', 'horario', 'evento']
        fields = '__all__'


class RegistrarAtividadeContinuaForm(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                required=False)

    class Meta:
        model = AtividadeContinua
        exclude = ['periodo', 'horario', 'evento']
        fields = '__all__'


class RegistrarAtividadeAdministrativaForm(forms.ModelForm):
    descricao = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                                required=False)

    class Meta:
        model = AtividadeAdministrativa
        exclude = ['periodo', 'horario', 'evento']
        fields = '__all__'


class RegistrarEspacoFisicoEventoForm(forms.ModelForm):
    nome = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
                           required=False)

    class Meta:
        model = EspacoFisico
        exclude = ['evento']
        fields = '__all__'
