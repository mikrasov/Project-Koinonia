# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=200)),
                ('istokenaction', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('current', models.CharField(max_length=200)),
                ('max', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('gmnotes', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('date_modified', models.DateTimeField(verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='character',
            name='pack',
            field=models.ForeignKey(to='manager.Pack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attribute',
            name='character',
            field=models.ForeignKey(to='manager.Character'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ability',
            name='character',
            field=models.ForeignKey(to='manager.Character'),
            preserve_default=True,
        ),
    ]
