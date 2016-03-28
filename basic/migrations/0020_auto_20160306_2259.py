# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0019_auto_20151110_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('updated', models.CharField(max_length=50, null=True, blank=True)),
                ('inserted', models.CharField(max_length=50, null=True, blank=True)),
                ('deleted', models.CharField(max_length=50, null=True, blank=True)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('deviceName', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Actions_field',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('deviceName', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Device List',
            },
        ),
        migrations.DeleteModel(
            name='SelectedSlug',
        ),
        migrations.RemoveField(
            model_name='titles',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='titles',
            name='slugGroups',
        ),
        migrations.RemoveField(
            model_name='titles',
            name='time_last_assessed',
        ),
        migrations.AddField(
            model_name='titles',
            name='expiry',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='titles',
            name='given',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=0, blank=True),
        ),
        migrations.AddField(
            model_name='titles',
            name='unique_key',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='answer_image',
            field=models.ImageField(upload_to='answer_as_images', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='answer_text',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='date_created',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='questions',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='titles',
            name='username',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
