# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_auto_20171220_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='ref_prod',
            new_name='ref_prod',
        ),
    ]
