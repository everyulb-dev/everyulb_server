from django.db import models
from customers import models as customer_model

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=250)
	customer = models.ForeignKey(customer_model.Customer,on_delete=models.CASCADE)

	def __str__(self):
		return self.name