# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0012_titles_sluggroups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
