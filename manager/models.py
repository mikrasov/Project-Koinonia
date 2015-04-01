from django.db import models


# Create your models here.
class Pack(models.Model):
    name = models.CharField(max_length=200)
    edition = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Character(models.Model):
    pack = models.ForeignKey(Pack)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True)
    gmnotes = models.TextField(blank=True)
    votes = models.IntegerField()
    source = models.CharField(max_length=200)


class Ability(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=200)
    action = models.TextField(blank=True)
    istokenaction = models.BooleanField(default=True)
    
class Attribute(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=200)
    current = models.CharField(max_length=200)
    max = models.CharField(max_length=200)