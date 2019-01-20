from django.db import models
from django.db.models import DO_NOTHING
from django.utils.timezone import now


from customers import models as customer_model

class ProjectType(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=250)
    customer = models.ForeignKey(customer_model.Customer,on_delete=models.CASCADE)
    type = models.OneToOneField(ProjectType, on_delete=DO_NOTHING)

    due_date = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name