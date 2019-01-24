# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Component
from .serializer import ComponentSerializer
from rest_framework import generics

from projects.api.serializer import ProjectSerializer
from reports.api.serializer import ReportSerializer
from reportcollections.api.serializer import ReportcollectionSerializer
from tasks.api.serializer import TaskSerializer
from reports.models import Report
from reportcollections.models import Reportcollection
from projects.models import Project
from tasks.models import Task

class ListCreateComponent(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class RetrieveUpdateDestroyComponent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class GetProjectComponent(APIView):
    def get(self, request, format=None):
        try:
            components = Component.objects.all()

            project_components_json = {}
            project_component_json = []

            for component in components:
                report = Report.objects.get(pk=component.report_id)
                report_collection = Reportcollection.objects.get(pk=report.project_id)
                project = Project.objects.get(pk=report_collection.project_id)

                temp_json = ComponentSerializer(component).data
                temp_json.update({
                    'project' : ProjectSerializer(project).data
                })
                project_component_json.append(temp_json)

            project_components_json.update({'project_components' : project_component_json})

            return Response(project_components_json)
        except Component.DoesNotExist:
            return Response({
                'project_components' : []
            })

class GetComponentTasks(APIView):
    def get(self, request, pk, format=None):
        try:
            tasks = Task.objects.filter(component_id=pk)

            component_tasks_json = {}
            component_tasks_list = []

            for task in tasks:
                component_tasks_list.append(TaskSerializer(task).data)

            component_tasks_json.update({
                "Tasks" : component_tasks_list
            })

            return Response(component_tasks_json)

        except Task.DoesNotExist:
            return Response({
                "Tasks" : []
            })

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
