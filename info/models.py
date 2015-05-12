import urllib, hashlib

from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    isPublic = models.BooleanField(default=True)
    website = models.URLField(blank=True, null=True)
    roll20_username = models.CharField(blank=True, null=True,max_length=200)
    about = models.TextField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('info:profile-detail', kwargs={'username': self.user.username})

    def getGravatar(self):
        return "http://www.gravatar.com/avatar/" + hashlib.md5(self.user.email.encode('utf-8').lower()).hexdigest() + "?";
    
    def get_owner(self):
        return self.user
    
    def is_public(self):
        return self.isPublic  
    
    def can_edit(self, user):
        return user.is_authenticated() and self.get_owner().username == user.username
        
    def can_view(self, user):
        return self.is_public() or self.can_edit(user)  
    
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)