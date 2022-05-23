from rest_framework import serializers
from .models import Melon, Bugs, Genie, Total, Youtube

class MelonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Melon
        fields = ('m_rank', 'm_song', 'm_artist', 'm_like', 'm_coverImg', 'm_date', 'm_time', 'm_weight')

class GenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genie
        fields = ('g_rank', 'g_song', 'g_artist', 'g_like', 'g_coverImg', 'g_date', 'g_time', 'g_weight')

class BugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = ('b_rank', 'b_song', 'b_artist', 'b_like', 'b_coverImg', 'b_date', 'b_time', 'b_weight')
class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = ('rank', 'song', 'artist', 'coverImg', 'date', 'time', 'weight')

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = ('song', 'link')