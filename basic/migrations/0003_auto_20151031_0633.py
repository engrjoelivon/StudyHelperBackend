# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20151031_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='priority',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)]),
        ),
    ]
