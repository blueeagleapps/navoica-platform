# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-14 16:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_creators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecreator',
            name='note',
            field=models.CharField(blank=True, help_text='Opcjonalne przypisy dotycz\u0105ce tego u\u017cytkownika (np. dlaczego zosta\u0142 mu odm\xf3wiony dost\u0119p do kreatora kursu)', max_length=512),
        ),
        migrations.AlterField(
            model_name='coursecreator',
            name='state',
            field=models.CharField(choices=[(b'unrequested', 'niepo\u017c\u0105dany'), (b'pending', 'oczekuj\u0105cy'), (b'granted', 'zaakceptowany'), (b'denied', 'odrzucony')], default=b'unrequested', help_text='Obecny stan kreatora kursu', max_length=24),
        ),
        migrations.AlterField(
            model_name='coursecreator',
            name='state_changed',
            field=models.DateTimeField(auto_now_add=True, help_text='Data ostatniej aktualizacji stanu', verbose_name=b'state last updated'),
        ),
        migrations.AlterField(
            model_name='coursecreator',
            name='user',
            field=models.OneToOneField(help_text='U\u017cytkownik Studio', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]