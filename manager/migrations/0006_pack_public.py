# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20150419_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
