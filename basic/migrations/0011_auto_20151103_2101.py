# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_auto_20151103_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='slugGroups',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
