# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acheteur', '0006_auto_20171220_1825'),
        ('Article', '0008_produit_marque_prod_id'),
        ('Relation_Acheteur_Article', '0002_auto_20171221_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_avis', models.PositiveIntegerField()),
                ('commantaire_avis', models.TextField(blank=True)),
                ('acheteur_avis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Acheteur.Acheteur')),
                ('produit_avis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit')),
            ],
        ),
        migrations.AlterField(
            model_name='panier',
            name='produit_panier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='quantite_prod_panier',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='produit_favori',
            name='produit_fav_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Produit'),
        ),
    ]