# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Acheteur', '0002_auto_20171220_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acheteur',
            old_name='telephone_ut',
            new_name='telephone_achet',
        ),
    ]
