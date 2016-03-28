# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20151101_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='no_of_time_accessed',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
