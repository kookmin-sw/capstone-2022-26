from django.shortcuts import render
from rest_framework.response import Response
from .models import ChartData
from rest_framework.views import APIView
from .serializer import DataSerializer

# Create your views here.
class DataListAPI(APIView):
    def get(self, request):
        queryset = ChartData.objects.all()
        print(queryset)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)