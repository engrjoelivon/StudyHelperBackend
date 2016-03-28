# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0015_titles_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
