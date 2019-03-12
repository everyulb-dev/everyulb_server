from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.

class UtilityCSV(models.Model):
    name = models.CharField(max_length=250)
    size = models.BigIntegerField(default=0)
    data = JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
