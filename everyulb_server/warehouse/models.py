from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class Warehouse(models.Model):
	name = models.CharField(max_length=250)
	data = JSONField()
	# has multiple report
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name