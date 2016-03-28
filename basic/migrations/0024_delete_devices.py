# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0023_userdevices'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Devices',
        ),
    ]
