# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Vendors

class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
        )
        model = Vendors

