# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Reportcollection

class ReportcollectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'project',
            'created_at',
            'updated_at',
        )
        model = Reportcollection

