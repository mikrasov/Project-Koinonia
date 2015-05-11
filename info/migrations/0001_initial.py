# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(default='user')),
                ('isPublic', models.BooleanField(default=True)),
                ('gravatar_url', models.URLField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('roll20_username', models.CharField(null=True, blank=True, max_length=200)),
                ('favorite_system', models.CharField(null=True, blank=True, max_length=200)),
                ('about', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
