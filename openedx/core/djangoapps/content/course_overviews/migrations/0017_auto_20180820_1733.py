# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-20 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0016_auto_20180817_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseoverview',
            old_name='category',
            new_name='course_category',
        ),
    ]
