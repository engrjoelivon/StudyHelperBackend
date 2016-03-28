# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0025_auto_20160312_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydevices',
            name='device_name',
            field=models.CharField(max_length=50, null=True, blank=True, unique=True),
        ),
    ]
