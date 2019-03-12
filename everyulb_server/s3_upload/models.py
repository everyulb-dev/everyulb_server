from django.db import models

# Create your models here.

class Upload(models.Model):
    name = models.CharField(max_length=250)
    extension = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    mimeType = models.CharField(max_length=250)
    webLink = models.CharField(max_length=1024)
    filePath = models.CharField(max_length=250)
    size = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name