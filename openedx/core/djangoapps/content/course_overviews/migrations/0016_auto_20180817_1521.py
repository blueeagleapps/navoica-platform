# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0015_courseoverview_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoverview',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='courseoverview',
            name='organizer',
            field=models.TextField(null=True),
        ),
    ]