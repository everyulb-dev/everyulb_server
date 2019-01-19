# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Map

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'report',
            'longitude',
            'latitude',
            'marker',
            'data',
            'created_at',
            'updated_at',
        )
        model = Map

