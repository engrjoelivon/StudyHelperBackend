# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0014_auto_20151107_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='username',
            field=models.CharField(unique=True, null=True, max_length=100),
        ),
    ]
