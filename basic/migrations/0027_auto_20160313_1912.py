# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0026_auto_20160313_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='unique_key',
            field=models.CharField(null=True, blank=True, unique=True, max_length=100),
        ),
    ]
