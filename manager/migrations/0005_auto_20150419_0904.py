# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20150413_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='avatar',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='token',
            field=models.URLField(blank=True),
        ),
    ]
