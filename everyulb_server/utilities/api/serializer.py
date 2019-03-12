# Author: Chirag Chamoli
# -*- coding: utf-8 -*-

from rest_framework import serializers
from ..models import UtilityCSV

class  UtilityCSVSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'size',
            'data',
            'created_at',
            'updated_at',
        )
        model = UtilityCSV