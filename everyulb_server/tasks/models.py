from django.db import models
from django.utils.timezone import now

from components import models as components_models
# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=250)
	component = models.ForeignKey(components_models.Component,on_delete=models.CASCADE)
	due_date = models.DateTimeField(default=now)
	# has components report
	def __str__(self):
		return self.name
