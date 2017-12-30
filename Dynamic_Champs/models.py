from django.core.validators import RegexValidator
from django.db import models


class Pays(models.Model):
    nom_pays = models.CharField(
        max_length=50,
        unique=True,
        help_text="Seulement des lettres",
        error_messages={
            'unique': "Une pays avec ce nom existe déjà.",
            'invalid': "Le nom doit contenir seulement des lettres"
        },
        validators=[
            RegexValidator(
                regex="^[a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïðòóôõöùúûüýÿ\s]+$"
            )
        ]
    )

    class Meta:
        ordering = ['nom_pays']

    def __str__(self):
        return self.nom_pays.capitalize()


class Marque(models.Model):
    nom_marque = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': "Une marque avec ce nom existe déjà.",
        },
    )

    class Meta:
        ordering = ['nom_marque']

    def __str__(self):
        return self.nom_marque.capitalize()


class Categorie(models.Model):
    nom_categ = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique': "Une catégorie avec ce nom existe déjà."
        },
    )
    description_categ = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ['nom_categ']

    def __str__(self):
        return self.nom_categ.capitalize()
