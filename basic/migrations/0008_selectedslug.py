# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0007_auto_20151101_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedSlug',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('slugname', models.CharField(null=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Slugname',
            },
        ),
    ]
