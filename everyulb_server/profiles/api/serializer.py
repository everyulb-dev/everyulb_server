# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'created_by',
            'updated_at',
        )
        model = Profile

