# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='slug',
        ),
    ]
