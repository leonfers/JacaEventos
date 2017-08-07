from rest_framework import serializers
from rest_framework.reverse import reverse
from core.models import Evento,Atividade

class EventosSerializer(serializers.ModelSerializer):

    dono = serializers.CharField(source='get_dono',read_only=True)
    tipo = serializers.CharField(source='get_tipo',read_only=True)
    valor = serializers.DecimalField(source='get_valor',read_only=True, max_digits=5, decimal_places=2,)

    class Meta:
        model = Evento
        fields = ('id','nome','dono','valor','tipo')

class AtividadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atividade
        fields = ('id','nome')