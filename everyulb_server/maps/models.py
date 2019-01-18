from django.contrib.postgres.fields import JSONField
from django.db import models
from reports import models as report_model
# Create your models here.
# Maps: project has many maps
class Map(models.Model):

	name = models.CharField(max_length=250)
	report = models.ForeignKey(report_model.Report,on_delete=models.CASCADE)
	longitude = models.DecimalField(max_digits=20,decimal_places=12)
	latitude =  models.DecimalField(max_digits=20,decimal_places=12)
	data = JSONField()
	def __str__(self):
		return self.name