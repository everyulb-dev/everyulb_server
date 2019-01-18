from django.db import models

# Create your models here.
class Vendors(models.Model):
    name = models.CharField(max_length=250)

    # has many employees
    # employees =

    def __str__(self):
        return self.name