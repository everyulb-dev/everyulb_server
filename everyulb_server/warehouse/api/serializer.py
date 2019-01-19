# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'data',
            'created_at',
            'updated_at',
        )
        model = Warehouse

