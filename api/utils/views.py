from rest_framework import viewsets, authentication, permissions
from utils.models import Periodo
from api.views import DefaultMixin
from .serializers import PeriodoSerializer


class PeriodoViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing periodos."""

    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    # filter_class = TaskFilter
    ordering_fields = ('id')