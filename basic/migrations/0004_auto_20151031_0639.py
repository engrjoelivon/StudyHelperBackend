# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20151031_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='difficulty',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)]),
        ),
    ]
