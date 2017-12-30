from django.contrib.auth.models import User
from django.db import models

from Dynamic_Champs.models import Pays


class Vendeur(User):
    registre_commerce_bout = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.first_name.title() + " " + self.last_name.capitalize()


class Boutique(models.Model):
    vendeur_bout_id = models.OneToOneField(
        Vendeur,
        on_delete=models.CASCADE,
    )
    nom_bout = models.CharField(
        max_length=254
    )
    adresse_bout = models.CharField(
        max_length=254,
        blank=True
    )
    description_bout = models.TextField(
        null=True,
        blank=True
    )
    pays_bout_id = models.ForeignKey(
        Pays
    )
    logo_bout = models.ImageField(
        upload_to="logo_boutique/",
        blank=True
    )

    def __str__(self):
        return self.nom_bout.capitalize()

    def save(self, *args, **kwargs):
        try:
            this = Boutique.objects.get(id=self.id)
            if this.logo_bout != self.logo_bout:
                this.logo_bout.delete(save=False)
        except:
            pass
        super(Boutique, self).save(*args, **kwargs)