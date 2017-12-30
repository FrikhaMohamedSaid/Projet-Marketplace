from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from Dynamic_Champs.models import Marque, Categorie
from Traitement.compression import compression_size_photo
from Vendeur.models import Boutique


def produit_directory_path(instance, filename):
    return 'Produits/{0}/{1}/'.format(instance.boutique_prod_id.nom_bout, filename)


class Produit(models.Model):
    ETAT = (
        ('N', "Nouveau"),
        ('O', "Occasion")
    )

    boutique_prod_id = models.ForeignKey(
        Boutique,
        on_delete=models.CASCADE,
    )
    titre_prod = models.CharField(
        max_length=254
    )
    ref_prod = models.CharField(
        max_length=254
    )
    marque_prod_id = models.ForeignKey(
        Marque,
        on_delete=models.CASCADE,
    )
    categorie_prod_id = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
    )
    description_prod = models.TextField(
        blank=True
    )
    prix_original_prod = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Le prix ne peut pas être négative!!"
            )
        ]
    )
    pourcentage_solde_prod = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        blank=True,
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Le pourcentage ne peut pas être négative!!"
            ),
            MaxValueValidator(
                limit_value=99,
                message="Valeur de pourcentage très élevé"
            )
        ]
    )
    quantite_stock_prod = models.PositiveSmallIntegerField()
    quantite_vendue_prod = models.PositiveSmallIntegerField(
        default=0
    )
    condition_prod = models.CharField(
        max_length=1,
        choices=ETAT
    )
    image_prod = models.ImageField(
        upload_to=produit_directory_path
    )
    nbr_avis_prod = models.PositiveSmallIntegerField(
        default=0
    )
    note_avis_prod = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0
    )

    def __str__(self):
        return self.titre_prod.capitalize()

    def save(self, *args, **kwargs):
        try:
            this = Produit.objects.get(id=self.id)
            if this.image_prod != self.image_prod:
                this.image_prod.delete(save=False)
        except:
            pass
        super(Produit, self).save(*args, **kwargs)
        # Compression du l'image du produit (max_widh = max_height = 512px)
        compression_size_photo(src=self.image_prod, size=512)

    def delete(self, using=None, keep_parents=False):
        this = Produit.objects.get(id=self.id)
        this.image_prod.delete(save=False)
        super(Produit, self).delete()



class Specification_Produit(models.Model):
    kle_value_spec_prod = models.TextField()
    produit_spec_prod = models.OneToOneField(
        Produit,
        on_delete=models.CASCADE,
    )