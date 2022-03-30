from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'