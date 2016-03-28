# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0024_delete_devices'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(null=True, max_length=50, blank=True)),
                ('device_name', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'UserDevices',
            },
        ),
        migrations.DeleteModel(
            name='UserDevices',
        ),
    ]
