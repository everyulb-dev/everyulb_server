# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Project
from .serializer import ProjectSerializer
from rest_framework import generics

class ListCreateProject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


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
