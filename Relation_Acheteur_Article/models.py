from django.db import models

from Acheteur.models import Acheteur
from Article.models import Produit


class Produit_Favori(models.Model):
    acheteur_fav_id = models.ForeignKey(
        Acheteur,
        # default=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    produit_fav_id = models.ForeignKey(
        Produit
    )
    date_heure_ajout_afv = models.DateTimeField(
        auto_now_add=True
    )


class Panier(models.Model):
    acheteur_panier_id = models.ForeignKey(
        Acheteur,
        on_delete=models.CASCADE
    )
    produit_panier_id = models.ForeignKey(
        Produit
    )
    quantite_prod_panier = models.PositiveIntegerField(
        default=0
    )


class Avis(models.Model):
    acheteur_avis_id = models.ForeignKey(
        Acheteur,
        on_delete=models.CASCADE
    )
    produit_avis_id = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE
    )
    note_avis = models.PositiveIntegerField()
    commantaire_avis = models.TextField(
        blank=True
    )

    # modifier valeur note avis
    def save(self, *args, **kwargs):
        this_produit = Produit.objects.get(pk=self.produit_avis_id_id)
        if not self.id:
            this_produit.note_avis_prod = ((this_produit.note_avis_prod * this_produit.nbr_avis_prod) + int(
                self.note_avis)) / (this_produit.nbr_avis_prod + 1)
            this_produit.nbr_avis_prod += 1
        else:
            this_avis = Avis.objects.get(pk=self.id)
            this_produit.note_avis_prod = ((this_produit.note_avis_prod * this_produit.nbr_avis_prod) - int(
                this_avis.note_avis) + int(self.note_avis)) / (this_produit.nbr_avis_prod)
        this_produit.save()
        super(Avis, self).save(*args, **kwargs)

    # modifier valeur note avis
    def delete(self, using=None, keep_parents=False):
        this_produit = Produit.objects.get(pk=self.produit_avis_id_id)
        if this_produit.nbr_avis_prod - 1 != 0:
            this_produit.note_avis_prod = ((this_produit.note_avis_prod * this_produit.nbr_avis_prod) - int(
                self.note_avis)) / (this_produit.nbr_avis_prod - 1)
        else:
            this_produit.note_avis_prod = 0
        this_produit.nbr_avis_prod -= 1
        this_produit.save()
        super(Avis, self).delete()
