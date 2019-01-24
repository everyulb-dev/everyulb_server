# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Project, ProjectType

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'customer',
            'type',
            'due_date',
            'created_at',
            'updated_at',
        )
        model = Project

class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
        )
