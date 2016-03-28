# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0011_auto_20151103_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='slugGroups',
            field=models.SlugField(null=True, unique=True, blank=True),
        ),
    ]
