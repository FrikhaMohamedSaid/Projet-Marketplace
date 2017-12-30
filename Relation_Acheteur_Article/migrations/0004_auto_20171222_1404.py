# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Relation_Acheteur_Article', '0003_auto_20171222_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='produit_avis_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='produit_panier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit'),
        ),
        migrations.AlterField(
            model_name='produit_favori',
            name='produit_fav_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit'),
        ),
    ]
