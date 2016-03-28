# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0030_auto_20160328_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='base',
            name='unique_key',
        ),
        migrations.RemoveField(
            model_name='base',
            name='username',
        ),
    ]
