# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Customer
from .serializer import CustomerSerializer
from rest_framework import generics

class ListCreateCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RetrieveUpdateDestroyCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RetriveCustomeProjet():
    # inline serialer
    pass




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
