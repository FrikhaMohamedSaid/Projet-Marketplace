# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0010_auto_20171225_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification_produit',
            name='produit_spec_prod',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit'),
        ),
    ]