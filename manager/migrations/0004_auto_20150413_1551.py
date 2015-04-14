# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20150413_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['name'], 'verbose_name_plural': 'attributes'},
        ),
        migrations.AlterUniqueTogether(
            name='ability',
            unique_together=set([('character', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('character', 'name')]),
        ),
    ]
