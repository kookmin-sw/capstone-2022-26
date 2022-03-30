from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import DataSerializer

# Create your views here.
# class DataListAPI(APIView):
#     def get(self, request):
#         