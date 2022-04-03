from django import views
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Chart, Track
from .serializer import ChartSerializer, TrackSerializer
from rest_framework.views import APIView

# Create your views here.
class ChartView(viewsets.ViewSet):
    queryset = Chart.objects.all()

    def list(self, request):
        chartData = {'tracks': [{'track': 'GANADARA (Feat. 아이유)', 'artist': '박재범', 'rank': 1, 'img_url':'https://cdnimg.melon.co.kr/cm2/album/images/108/89/981/10889981_20220311110820_500.jpg/melon/resize/120/quality/80/optimize'}]}
        return Response(chartData)
    

    @action(detail=False, methods=['get'])
    def melon(self, request):
        melonChartData = {'site':'Melon', 'tracks': [{'track': 'GANADARA (Feat. 아이유)', 'artist': '박재범', 'rank': 1, 'like':86592, 'img_url':'https://cdnimg.melon.co.kr/cm2/album/images/108/89/981/10889981_20220311110820_500.jpg/melon/resize/120/quality/80/optimize'}]}
        return Response(melonChartData)

    @action(detail=False, methods=['get'])
    def bugs(self, request):
        chartData = {'name':'bugs', 'artist': 'a', 'rank': 1, 'like':1, 'img_url':'https://aa.com'}
        return Response(chartData)

    @action(detail=False, methods=['get'])
    def genie(self, request):
        chartData = {'name':'genie', 'artist': 'a', 'rank': 1, 'like':1, 'img_url':'https://aa.com'}
        return Response(chartData)


class TrackView(APIView):
    queryset = Track.objects.all()
    def get(self, request, pk):
        param = request.GET.get('artist')
        trackData = {'track':pk, 'artist': param, 'rank': [{'site': 'Melon', 'dayBefore': 2, 'yesterday': 2, 'today': 1}, {'site': 'Bugs', 'dayBefore': 3, 'yesterday': 4, 'today': 4}, {'site': 'Genie', 'dayBefore': 2, 'yesterday': 2, 'today': 3}]}
        return Response(trackData)