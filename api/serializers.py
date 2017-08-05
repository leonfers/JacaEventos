from datetime import date
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from core.models import Evento

User = get_user_model()

class EventosSerializer(serializers.ModelSerializer):

    dono = serializers.CharField(source='get_dono',read_only=True)
    tipo = serializers.CharField(source='get_tipo',read_only=True)
    class Meta:
        model = Evento
        fields = ('id','nome','dono','valor','tipo')

class UserSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    nome = serializers.CharField(source='get_nome_completo', read_only=True)


    def get_links(self, obj):

        request = self.context['request']
        username = obj.get_username()

        return {
            'self': reverse('usuario-detail',kwargs= {User.USERNAME_FIELD: username }, request=request)
        }
    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'nome', 'is_active','links',)