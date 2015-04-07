# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_character_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='source',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
