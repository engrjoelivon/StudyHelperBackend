# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0021_auto_20160310_0754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices',
            old_name='deviceName',
            new_name='device_name',
        ),
    ]
