from django.db import models
from customers import models as customer_model
# Create your models here.
class Reportcollection(models.Model):
	name = models.CharField(max_length=250)
	# has multiple report
	# belongs to a Customer
	project = models.ForeignKey(customer_model.Customer,on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name