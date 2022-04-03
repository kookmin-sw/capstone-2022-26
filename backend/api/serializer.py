from rest_framework import serializers
from .models import Chart, Track

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ('id', 'name', 'artist', 'rank', 'like', 'img_url')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'artist', 'genre', 'img_url', 'daybefore_rank', 'yesterday_rank', 'today_rank')

