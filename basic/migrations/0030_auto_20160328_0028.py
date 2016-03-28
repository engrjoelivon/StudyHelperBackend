# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0029_auto_20160317_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(null=True, blank=True, max_length=50)),
                ('unique_key', models.CharField(null=True, blank=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Base Class',
            },
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
