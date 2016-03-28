# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_selectedslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='slugGroups',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
