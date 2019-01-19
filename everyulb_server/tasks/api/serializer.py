# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'component',
            'due_date',
            'created_by',
            'assigned_to',
            'created_at',
            'assigned_to',
        )
        model = Task

