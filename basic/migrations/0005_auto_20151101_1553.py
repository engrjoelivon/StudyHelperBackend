# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20151031_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='difficulty',
            field=models.PositiveSmallIntegerField(blank=True, default=1, choices=[(1, 1), (2, 2), (3, 3)]),
        ),
        migrations.RemoveField(
            model_name='titles',
            name='groupname',
        ),
        migrations.AddField(
            model_name='titles',
            name='groupname',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='no_of_time_accessed',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='priority',
            field=models.IntegerField(blank=True, default=1, choices=[(1, 1), (2, 2), (3, 3)]),
        ),
        migrations.RemoveField(
            model_name='titles',
            name='questions',
        ),
        migrations.AddField(
            model_name='titles',
            name='questions',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
