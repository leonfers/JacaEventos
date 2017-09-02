from .serializers import EventosSerializer, AtividadeSerializer
from core.models import Evento, AtividadePadrao
from rest_framework import viewsets, authentication, permissions
from api.views import DefaultMixin

class EventoViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing eventos."""

    queryset = Evento.objects.all()
    serializer_class = EventosSerializer
    # filter_class = TaskFilter
    search_fields = ('nome')
    ordering_fields = ('id')


class AtividadeViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing atividades."""

    queryset = AtividadePadrao.objects.all()
    serializer_class = AtividadeSerializer
    search_fields = ('nome')
    ordering_fields = ('id')

