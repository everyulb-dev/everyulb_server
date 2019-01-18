from django.db import models
from django.db.models import DO_NOTHING
from django.utils.timezone import now
from profiles import models as profile_model
from components import models as components_models
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=250)
    component = models.ForeignKey(components_models.Component,on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=now)

    created_by = models.ForeignKey(profile_model.Profile,on_delete=DO_NOTHING,related_name='created_by')
    assigned_to = models.ForeignKey(profile_model.Profile, on_delete=DO_NOTHING,related_name='assigned_to')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # has components report
    def __str__(self):
        return self.name
