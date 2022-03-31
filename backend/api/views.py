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
        chartData = {'name':'n', 'artist': 'a', 'rank': 1, 'like':1, 'img_url':'https://aa.com'}
        return Response(chartData)
    

    @action(detail=False, methods=['get'])
    def melon(self, request):
        chartData = {'name':'melon', 'artist': 'a', 'rank': 1, 'like':1, 'img_url':'https://aa.com'}
        return Response(chartData)

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
        return Response(pk + ' ' + param)