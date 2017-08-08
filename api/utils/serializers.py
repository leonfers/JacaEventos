from rest_framework import serializers
from rest_framework.reverse import reverse
from utils.models import Periodo

class PeriodoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Periodo
        fields = '__all__'