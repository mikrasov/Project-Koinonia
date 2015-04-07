# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20150401_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='votes',
        ),
    ]
