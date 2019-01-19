# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'customer',
            'type',
            'created_at',
            'updated_at',
        )
        model = Project

