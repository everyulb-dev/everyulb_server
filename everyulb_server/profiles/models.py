from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from everyulb_server.settings import AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    # Changes in this field due to CustomUser model in users app.
    # Ref : https://stackoverflow.com/questions/46562402/fields-e301-field-defines-a-relation-with-the-model-auth-user-which-has-bee
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()