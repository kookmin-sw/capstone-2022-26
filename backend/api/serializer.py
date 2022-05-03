from rest_framework import serializers
from .models import Melon, Bugs, Genie

class MelonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Melon
        fields = ('rank', 'song', 'artist', 'like', 'coverImg', 'crawlingTime')

class GenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genie
        fields = ('rank', 'song', 'artist', 'like', 'coverImg', 'crawlingTime')

class BugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = ('rank', 'song', 'artist', 'like', 'coverImg', 'crawlingTime')