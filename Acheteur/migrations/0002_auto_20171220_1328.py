# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 12:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acheteur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acheteur',
            name='adresse_achet',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='acheteur',
            name='telephone_ut',
            field=models.CharField(default=0, max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\+[1-9][0-9]{1,2}[ ])?[0-9]{6,}$')]),
            preserve_default=False,
        ),
    ]
