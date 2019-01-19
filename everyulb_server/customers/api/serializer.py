# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from rest_framework import serializers
from ..models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'sub_domian',
            'has_public_module',
            'logo',
            'brand_primary_color',
            'brand_secondry_color',
            'website',
            'bio',
            'legal_name',
            'point_of_contact',
            'created_at',
            'updated_at',
        )
        model = Customer

