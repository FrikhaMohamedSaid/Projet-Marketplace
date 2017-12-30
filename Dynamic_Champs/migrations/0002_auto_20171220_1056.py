# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 09:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dynamic_Champs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom_categ',
            field=models.CharField(error_messages={'unique': 'Une catégorie avec ce nom existe déjà.'}, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='pays',
            name='nom_pays',
            field=models.CharField(error_messages={'invalid': 'Le nom doit contenir seulement des lettres', 'unique': 'Une pays avec ce nom existe déjà.'}, help_text='Seulement des lettres', max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïðòóôõöùúûüýÿ\\s]+$')]),
        ),
    ]