# Author: Chirag Chamoli
# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Customer
from .serializer import CustomerSerializer

class ListCustomers(APIView):
    def get(self,request,format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)