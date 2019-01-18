from django.db import models

# Create your models here.
# Customers
# Customers: customers has many profiles
class Customer(models.Model):
    name = models.CharField(max_length=250)
    sub_domian = models.CharField(max_length=30)
    has_public_module = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='logos/')
    brand_primary_color = models.CharField(max_length=10)
    brand_secondry_color = models.CharField(max_length=10)
    website = models.URLField(max_length=10)
    bio = models.CharField(max_length=1000)
    legal_name = models.CharField(max_length=1000)

    # has many projects
    # has many vendors
    # vendors =
    # has many employees
    # employees =

    def __str__(self):
        return self.name




