# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Project, ProjectType
from .serializer import ProjectSerializer, ProjectTypeSerializer
from rest_framework import generics

from django.forms.models import model_to_dict


from components.api.serializer import ComponentSerializer
from maps.api.serializer import MapSerializer
from tasks.api.serializer import TaskSerializer
from reports.api.serializer import ReportSerializer
from reportcollections.api.serializer import ReportcollectionSerializer
from components.models import Component
from tasks.models import Task
from maps.models import Map
from reports.models import Report
from reportcollections.models import Reportcollection
from profiles.models import Profile

class ListCreateProject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class GetProjectDetails(APIView):
    def get(self, request, format=None):
        try:
            projects = Project.objects.all()

            project_details_json = {}
            project_details_list = []


            for project in projects:

                temp_json = ProjectSerializer(project).data

                # Project Type [execution, survey, impact analysis, etc.]
                project_type = ProjectType.objects.get(pk=project.type_id)
                temp_json.update({"type" : project_type.name})

                reportcollection = Reportcollection.objects.get(project_id=project.id)

                # for reportcollection in reportcollections:
                report = Report.objects.get(project_id=reportcollection.id)

                # for report in reports:
                component = Component.objects.get(report_id=report.id)

                # Just once. Need to confirm how to know location name.
                # This is one-to-many relationship with report.
                maps = Map.objects.get(report_id=report.id)
                temp_json.update({"location" : maps.name})

                # for component in components:
                task = Task.objects.get(component_id=component.id)

                profile = Profile.objects.get(pk=task.assigned_to_id)
                task_assigned_to = profile.user.username
                # for task in tasks:
                # if task.assigned_to not in task_assigned_to:
                #     task_assigned_to.append(task.assigned_to)
                temp_json.update({"assigned_to" : task_assigned_to})

                project_details_list.append(temp_json)

            project_details_json.update({"Project Details" : project_details_list})
            return Response(project_details_json)
        except Project.DoesNotExist:
            return Response({"Project Details" : []})


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
