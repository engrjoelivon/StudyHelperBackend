# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0027_auto_20160313_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='old_updated_key',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
