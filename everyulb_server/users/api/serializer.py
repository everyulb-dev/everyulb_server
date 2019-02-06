# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'email',
            'username',
        )
        model = CustomUser

