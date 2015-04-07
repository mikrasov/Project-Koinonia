# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20150406_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='edition',
            new_name='system',
        ),
    ]
