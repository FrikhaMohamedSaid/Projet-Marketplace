from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from Dynamic_Champs.models import Pays


class Adresse(models.Model):
    num_adr = models.CharField(
        max_length=10
    )
    ville_adr = models.CharField(
        max_length=254
    )
    code_postale_adr = models.PositiveIntegerField()
    pays_adr = models.ForeignKey(
        Pays,
        on_delete=models.CASCADE
    )


class Acheteur(User):
    adresse_achet_id = models.ForeignKey(
        Adresse,
        null=True,
        on_delete=models.CASCADE,
    )
    telephone_achet = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(regex="^(\+[1-9][0-9]{1,2}[ ])?[0-9]{6,}$")
        ]
    )

    def __str__(self):
        return self.first_name.title() + " " + self.last_name.capitalize()


class Livraison(models.Model):
    PAYEMENT = (
        ('', "A Domicile"),
        ('', "Par Virement"),
        ('', "Carte Bancaire")
    )

    acheteur_livrai_id = models.ForeignKey(
        Acheteur,
        on_delete=models.CASCADE,
    )
    adresse_livrai_id = models.ForeignKey(
        Adresse,
        null=True,
        on_delete=models.CASCADE,
    )
    num_carte_livrai = models.CharField(
        max_length=254,
        blank=True
    )
    type_payement_livrai = models.CharField(
        max_length=50,
        choices=PAYEMENT
    )