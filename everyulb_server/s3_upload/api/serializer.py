# Author: Chirag Chamoli
# -*- coding: utf-8 -*-

from rest_framework import serializers
from ..models import Upload

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'extension',
            'title',
            'mimeType',
            'webLink',
            'filePath',
            'size',
            'created_at',
            'updated_at',
        )
        model = Upload