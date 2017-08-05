from .serializers import EventosSerializer
from core.models import Evento
from rest_framework import viewsets, authentication, permissions
from api.views import DefaultMixin

class EventoViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):

    queryset = Evento.objects.all()
    serializer_class = EventosSerializer
    # filter_class = TaskFilter
    search_fields = ('nome')
    ordering_fields = ('id')