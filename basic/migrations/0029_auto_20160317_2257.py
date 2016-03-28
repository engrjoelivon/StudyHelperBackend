# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0028_actions_old_updated_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydevices',
            name='device_name',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]
