# Author: Chirag Chamoli
# -*- coding: utf-8 -*-


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from ..models import UtilityCSV
from .serializer import UtilityCSVSerializer

import csv
import json
import os
import pandas as pd
import json

class CSVToJSON(APIView):
    parser_classes = (MultiPartParser, )

    def get(self, request, format=None):
        query = UtilityCSV.objects.all()
        serilaizer = UtilityCSVSerializer(query, many=True)
        return Response(serilaizer.data)

    def post(self, request, format=None):

        file_obj = request.FILES['file']
        filename = file_obj.name
        filesize = file_obj.size

        dataframe = pd.read_csv(file_obj)
        filedata = dataframe.to_json(orient='records')

        object = {}
        object['name'] = filename
        object['size'] = filesize
        object['data'] = filedata
        serializer = UtilityCSVSerializer(data=object)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CSVToJSONId(APIView):
    def get(self, request, id, format=None):
        query = UtilityCSV.objects.get(id=id)
        serilaizer = UtilityCSVSerializer(query)

        return Response(serilaizer.data)

    def delete(self, request, id, format=None):
        query = UtilityCSV.objects.get(id=id)
        query.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)