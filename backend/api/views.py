from django import views
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Melon, Genie, Bugs
from .serializer import MelonSerializer, GenieSerializer, BugsSerializer
from rest_framework.views import APIView

# Create your views here.
class ChartView(viewsets.ViewSet):
    melon_queryset = Melon.objects
    bugs_queryset = Bugs.objects
    genie_queryset = Genie.objects

    def list(self, request):
        chartData = {'name':'통합', 'artist': 'a', 'rank': 1, 'like':1, 'img_url':'https://aa.com'}
        return Response(chartData)
    

    @action(detail=False, methods=['get'])
    def melon(self, request):
        queryset = self.melon_queryset.order_by('-id')[:100]
        # queryset = queryset.order_by('id')
        serialized_melon = MelonSerializer(queryset, many=True)
        return Response(data=serialized_melon.data)

    @action(detail=False, methods=['get'])
    def bugs(self, request):
        queryset = self.genie_queryset.order_by('-id')[:100]
        serialized_genie = BugsSerializer(queryset, many=True)
        return Response(data=serialized_genie.data)

    @action(detail=False, methods=['get'])
    def genie(self, request):
        queryset = self.bugs_queryset.order_by('-id')[:100]
        serialized_genie = GenieSerializer(queryset, many=True)
        return Response(data=serialized_genie.data)


class TrackView(APIView):
    def get(self, request, pk):
        param = request.GET.get('artist')
        melon_queryset = Melon.objects.filter(song=pk, artist=param)
        bugs_queryset = Bugs.objects.filter(song=pk, artist=param)
        genie_queryset = Genie.objects.filter(song=pk, artist=param)

        serialized_melon = MelonSerializer(melon_queryset, many=True)
        serialized_bugs = MelonSerializer(bugs_queryset, many=True)
        serialized_genie = MelonSerializer(genie_queryset, many=True)

        trackData = {'track':pk, 'artist':param, 'rank': [{'site': 'Melon', 'dayBefore': serialized_melon.data[0]['rank'], 'yesterday': serialized_melon.data[1]['rank'], 'today': serialized_melon.data[2]['rank']},
        {'site': 'Bugs', 'dayBefore': serialized_bugs.data[0]['rank'], 'yesterday': serialized_bugs.data[1]['rank'], 'today': serialized_bugs.data[2]['rank']},
        {'site': 'Genie', 'dayBefore': serialized_genie.data[0]['rank'], 'yesterday': serialized_genie.data[1]['rank'], 'today': serialized_genie.data[2]['rank']}]}

        return Response(data=trackData)