from rest_framework import serializers
from .models import ChartData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartData
        fields = '__all__'