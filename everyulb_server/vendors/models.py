from django.db import models

# Create your models here.
class Vendors(models.Model):
    name = models.CharField(max_length=250)
    # has many employees
    # employees =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name