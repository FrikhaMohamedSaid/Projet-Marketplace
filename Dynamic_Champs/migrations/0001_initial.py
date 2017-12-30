# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 21:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categ', models.CharField(max_length=100, unique=True)),
                ('description_categ', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pays', models.CharField(help_text='Seulement des lettres', max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïðòóôõöùúûüýÿ\\s]+$')])),
            ],
        ),
    ]
