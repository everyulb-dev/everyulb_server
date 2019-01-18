from django.db import models
from reportcollections import models as reportcollections_model
# Create your models here.
class Report(models.Model):
	name = models.CharField(max_length=250)
	# has many components
	# belongs to a Reportcollection
	project = models.ForeignKey(reportcollections_model.Reportcollection,on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name