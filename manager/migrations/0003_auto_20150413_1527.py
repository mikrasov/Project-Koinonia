# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20150409_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='slug',
            field=models.SlugField(default='character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='viewKey',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='pack',
            name='slug',
            field=models.SlugField(default='pack'),
        ),
        migrations.AlterField(
            model_name='pack',
            name='viewKey',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterUniqueTogether(
            name='character',
            unique_together=set([('pack', 'name')]),
        ),
    ]
