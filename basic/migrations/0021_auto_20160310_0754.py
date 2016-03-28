# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0020_auto_20160306_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='time_last_given',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='expiry',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='username',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
