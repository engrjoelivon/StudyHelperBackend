# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0017_auto_20151109_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='userName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='groups',
            name='slugGroups',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
