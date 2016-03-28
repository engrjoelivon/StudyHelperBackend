# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20151101_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='groupname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
