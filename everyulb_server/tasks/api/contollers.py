# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Task
from .serializer import TaskSerializer
from rest_framework import generics

from projects.api.serializer import ProjectSerializer
from reports.api.serializer import ReportSerializer
from reportcollections.api.serializer import ReportcollectionSerializer
from components.api.serializer import ComponentSerializer
from reports.models import Report
from reportcollections.models import Reportcollection
from projects.models import Project
from components.models import Component

class ListCreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RetrieveUpdateDestroyTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GetProjectTasks(APIView):
    def get(self, request, format=None):
        try:
            tasks = Task.objects.all()

            project_task_json = {}
            project_task_list = []

            for task in tasks:
                component = Component.objects.get(pk=task.component_id)
                report = Report.objects.get(pk=component.report_id)
                report_collection = Reportcollection.objects.get(pk=report.project_id)
                project = Project.objects.get(pk=report_collection.project_id)

                temp_json = TaskSerializer(task).data
                temp_json.update({'project' : ProjectSerializer(project).data})

                project_task_list.append(temp_json)

            project_task_json.update({'project_task' : project_task_list})
            return Response(project_task_json)
        except Task.DoesNotExist:
            return Response({'project_task' : []})

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
