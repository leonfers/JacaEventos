from datetime import date
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    nome = serializers.CharField(source='get_nome_completo', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'nome', 'is_active')
    def get_links(self, obj):

        request = self.context['request']
        return {
            'self': reverse('user-detail',kwargs= {User.USERNAME_FIELD: username }, request=request)
        }
