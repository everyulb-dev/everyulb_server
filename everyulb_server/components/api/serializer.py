# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Component

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'report',
            'name',
            'is_milestone',
            'amount_allocated',
            'amount_used',
            'data',
            'created_at',
            'updated_at',
        )
        model = Component

