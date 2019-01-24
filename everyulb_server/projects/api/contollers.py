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

                reportcollections = Reportcollection.objects.filter(project_id=project.id)

                for reportcollection in reportcollections:
                    reports = Report.objects.filter(project_id=reportcollection.id)

                    for report in reports:
                        components = Component.objects.filter(report_id=report.id)

                        maps = Map.objects.filter(report_id=report.id)
                        temp_map_list = []

                        for map in maps:
                            coordinates = {"longitude": map.longitude,
                                            "latitude": map.latitude}
                            temp_map_list.append(coordinates)

                        temp_json.update({
                            "maps" : temp_map_list
                        })

                        for component in components:
                            tasks = Task.objects.filter(component_id=component.id)


                            task_assigned_to = []
                            for task in tasks:
                                profiles = Profile.objects.filter(pk=task.assigned_to_id)
                                for profile in profiles:
                                    if profile.user.username not in task_assigned_to:
                                        task_assigned_to.append(profile.user.username)
                            temp_json.update({
                                "profile" :
                                    {"assigned_to" : task_assigned_to}
                                })

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
