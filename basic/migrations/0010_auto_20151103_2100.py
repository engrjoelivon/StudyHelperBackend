# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_groups_sluggroups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='groupName',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
