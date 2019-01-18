from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class Warehouse(models.Model):
	name = models.CharField(max_length=250)
	data = JSONField()
	# has multiple report
	def __str__(self):
		return self.name