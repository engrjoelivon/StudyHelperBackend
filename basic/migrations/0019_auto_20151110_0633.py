# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0018_auto_20151110_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='questions',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
