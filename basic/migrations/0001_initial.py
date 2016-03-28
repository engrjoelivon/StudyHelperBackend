# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('groupName', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'groupName',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('questionname', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'questionname',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('difficulty', models.PositiveSmallIntegerField(blank=True)),
                ('priority', models.PositiveSmallIntegerField(blank=True)),
                ('answer_text', models.TextField(blank=True, max_length=1000)),
                ('answer_image', models.ImageField(blank=True, upload_to='answer_as_images')),
                ('no_of_time_accessed', models.PositiveSmallIntegerField(blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('time_last_assessed', models.DateField(auto_now=True)),
                ('groupname', models.ManyToManyField(to='basic.Groups')),
                ('questions', models.ManyToManyField(to='basic.Questions')),
            ],
            options={
                'verbose_name': 'Title',
            },
        ),
    ]
