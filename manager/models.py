from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pack(models.Model):
    owner = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    system = models.CharField(max_length=200)

    def __str__(self):
        return '%s (%s)' % (self.name, self.system)
        
class Character(models.Model):
    pack = models.ForeignKey(Pack)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, unique=True)
    source = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    gmnotes = models.TextField(blank=True)
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return '%s (%s)' % (self.name, self.source)

class Ability(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=200)
    action = models.TextField(blank=True)
    istokenaction = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "abilities"
        
    def __str__(self):
        return '%s' % self.name
    
class Attribute(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=200)
    current = models.CharField(max_length=200)
    max = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "atributes"
    
    def __str__(self):
        return '%s' % self.name