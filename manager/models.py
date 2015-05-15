import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Pack(models.Model):
    viewKey = models.UUIDField(unique=True, default=uuid.uuid4)
    isPublic = models.BooleanField(default=True)
    
    owner = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='pack') 
    
    name = models.CharField(max_length=200)
    system = models.CharField(max_length=200)

    def __str__(self):
        return '%s (%s)' % (self.name, self.system)
    
    def get_secret_url(self):
        return reverse('manager:pack-detail', kwargs={'pk': self.id, 'slug':self.slug})+"?p="+str(self.viewKey)

    def get_absolute_url(self):
        return reverse('manager:pack-detail', kwargs={'pk': self.id, 'slug':self.slug})

    def get_absolute_update_url(self):
        return reverse('manager:pack-update', kwargs={'pk': self.id, 'slug':self.slug})
    
    def get_absolute_delete_url(self):
        return reverse('manager:pack-delete', kwargs={'pk': self.id, 'slug':self.slug})

    def get_absolute_import_url(self):
        return reverse('manager:pack-import', kwargs={'pk': self.id, 'slug':self.slug})

    def get_absolute_export_url(self):
        return reverse('manager:pack-export', kwargs={'pk': self.id, 'slug':self.slug})
    
    def get_owner(self):
        return self.owner
    
    def is_public(self):
        return self.isPublic     
    
    def can_edit(self, user):
        return user.is_authenticated() and self.get_owner().username == user.username
        
    def can_view(self, user, viewPass=""):
        return self.is_public() or self.can_edit(user) or viewPass == str(self.viewKey)
    
class Character(models.Model):
    viewKey = models.UUIDField(unique=True, default=uuid.uuid4)

    pack = models.ForeignKey(Pack)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='character') 
    
    name = models.CharField(max_length=200)
    avatar = models.URLField(blank=True)
    token = models.URLField(blank=True)
    source = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    gmnotes = models.TextField(blank=True)
    
    class Meta:
        ordering = ["name"]
        unique_together = ("pack", "name")
        
    def __str__(self):
        return '%s (%s)' % (self.name, self.source)
    
    def get_secret_url(self):
        return reverse('manager:character-detail', kwargs={'pk': self.id, 'slug':self.slug})+"?p="+str(self.viewKey)

    def get_absolute_url(self):
        return reverse('manager:character-detail', kwargs={'pk': self.id, 'slug':self.slug})

    def get_absolute_update_url(self):
        return reverse('manager:character-update', kwargs={'pk': self.id, 'slug':self.slug})
    
    def get_absolute_delete_url(self):
        return reverse('manager:character-delete', kwargs={'pk': self.id, 'slug':self.slug})

    def get_absolute_export_url(self):
        return reverse('manager:character-export', kwargs={'pk': self.id, 'slug':self.slug})
    
    def get_owner(self):
        return self.pack.owner
    
    def is_public(self):
        return self.pack.isPublic      
    
    def can_edit(self, user):
        return user.is_authenticated() and self.get_owner().username == user.username
        
    def can_view(self, user, viewPass=""):
        return self.is_public() or self.can_edit(user) or viewPass == str(self.viewKey)
    
class Ability(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=200)
    action = models.TextField(blank=True)
    istokenaction = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "abilities"
        unique_together = ("character", "name")
        
    def __str__(self):
        return '%s' % self.name
    
class Attribute(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=200)
    current = models.CharField(max_length=200)
    max = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "attributes"
        unique_together = ("character", "name")
    
    def __str__(self):
        return '%s' % self.name