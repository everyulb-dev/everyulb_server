# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Map
from .serializer import MapSerializer
from rest_framework import generics

class ListCreateMap(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class RetrieveUpdateDestroyMap(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

