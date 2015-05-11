# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20150511_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gravatar_url',
        ),
    ]
