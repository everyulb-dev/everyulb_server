# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Task
from .serializer import TaskSerializer
from rest_framework import generics

class ListCreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RetrieveUpdateDestroyTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



# Ignore this below.
# class ListCreateCustomers(APIView):
#     def get(self,request,format=None):
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers,many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CustomerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
