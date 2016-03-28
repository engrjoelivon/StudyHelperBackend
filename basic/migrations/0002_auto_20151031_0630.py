# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='groupName',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionname',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
