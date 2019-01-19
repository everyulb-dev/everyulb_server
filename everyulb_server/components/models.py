from django.contrib.postgres.fields import JSONField
from django.db import models
from reports import models as report_model
# Create your models here.
class Component(models.Model):
    # belongs to report

    report = models.ForeignKey(report_model.Report,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    is_milestone = models.BooleanField(default=False)
    amount_allocated = models.IntegerField(default=0, help_text = "Add in Paisa")
    amount_used = models.IntegerField(default=0, help_text = "Add in Paisa")
    data = JSONField()

    # belongs to a report
    # has many tasks

    status = (
        ('planning', 'Planning'),
        ('execution', 'Execution'),
        ('impact', 'Impact'),

    )
    status = models.CharField(
        max_length=50,
        choices=status,
        default='planning',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
