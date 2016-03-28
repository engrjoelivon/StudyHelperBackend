# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0013_auto_20151107_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
