# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('action', models.TextField(blank=True)),
                ('istokenaction', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'abilities',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('current', models.CharField(max_length=200)),
                ('max', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'atributes',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('bio', models.TextField(blank=True)),
                ('gmnotes', models.TextField(blank=True)),
                ('source', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('system', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
