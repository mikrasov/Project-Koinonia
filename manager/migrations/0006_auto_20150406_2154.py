# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20150406_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'verbose_name_plural': 'abilities', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name_plural': 'atributes', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['name']},
        ),
    ]
