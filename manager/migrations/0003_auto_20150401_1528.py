# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_character_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 1, 22, 27, 47, 405306, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 22, 27, 57, 831628, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='source',
            field=models.CharField(default=datetime.datetime(2015, 4, 1, 22, 28, 5, 905609, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pack',
            name='edition',
            field=models.CharField(default=datetime.datetime(2015, 4, 1, 22, 28, 11, 914711, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ability',
            name='action',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ability',
            name='istokenaction',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='bio',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='gmnotes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='votes',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pack',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pack',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
