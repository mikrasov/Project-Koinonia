# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_pack_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='public',
            new_name='isPublic',
        ),
    ]
