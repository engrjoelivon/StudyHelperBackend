# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0016_auto_20151109_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='slugGroups',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
