# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0022_auto_20160310_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDevices',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('device_name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'UserDevices',
            },
        ),
    ]
