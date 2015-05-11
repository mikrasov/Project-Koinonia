from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    isPublic = models.BooleanField(default=True)
    website = models.URLField(blank=True, null=True)
    roll20_username = models.CharField(blank=True, null=True,max_length=200)
    favorite_system = models.CharField(blank=True, null=True,max_length=200)
    about = models.TextField(blank=True, null=True)
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)