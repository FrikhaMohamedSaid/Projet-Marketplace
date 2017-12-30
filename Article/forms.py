from django import forms

from Article.models import Produit
from Dynamic_Champs.models import Marque, Categorie


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [
            'titre_prod',
            'ref_prod',
            'marque_prod_id',
            'categorie_prod_id',
            'description_prod',
            'quantite_stock_prod',
            'prix_original_prod',
            'pourcentage_solde_prod',
            'condition_prod',
            'image_prod'
        ]
        labels = {
            'titre_prod': "Titre de l'article",
            'ref_prod': "Référence",
            'marque_prod_id': "Marque",
            'categorie_prod_id': "Catégorie",
            'description_prod': "Description",
            'quantite_stock_prod': "Quantité dans le stock",
            'prix_original_prod': "Prix original de l'unité",
            'pourcentage_solde_prod': "Remise en %",
            'condition_prod': "Condition",
            'image_prod': "Photo"
        }
        widgets = {
            'titre_prod': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'ref_prod': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'marque_prod_id': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'categorie_prod_id': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'description_prod': forms.Textarea(
                attrs={
                    'class': "form-control"
                }
            ),
            'quantite_stock_prod': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),

            'pourcentage_solde_prod': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'prix_original_prod': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'condition_prod': forms.Select(
                attrs={
                    'class': "form-control"
                }
            )
        }


class FilterProduitForm(forms.Form):
    AVIS = (
        ('1', "1 étoiles et +"),
        ('2', "2 étoiles et +"),
        ('3', "3 étoiles et +"),
        ('4', "4 étoiles et +"),
        ('5', "5 étoiles"),
    )

    condition_prod = forms.ChoiceField(
        label="Neuf ou occasion",
        choices=Produit.ETAT,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'onclick': "this.form.submit()",
            }
        )
    )
    prix_min_prod = forms.IntegerField(
        label="Prix Minimal (TND)",
        widget=forms.NumberInput(
            attrs={
                'type': "range",
                'min': "0",
                'max': "1000",
                'step': '5',
                'onmouseup': "this.form.submit()",
                'class': "form-control"
            },
        )
    )
    marque_prod = forms.ModelMultipleChoiceField(
        label="Marque",
        queryset=Marque.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'onclick': "this.form.submit()"
            }
        )
    )
    categorie_prod = forms.ModelChoiceField(
        label="Catégorie",
        queryset=Categorie.objects.all(),
        empty_label="Toutes nos catégories",
        widget=forms.Select(
            attrs={
                'onchange': "this.form.submit()",
                'class': "form-control"
            }
        )
    )
    avis_prod = forms.ChoiceField(
        label="Avis clients",
        choices=AVIS,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'onclick': "this.form.submit()"
            }
        )
    )

    def __init__(self, avis_choices=AVIS, **kwargs):
        self.base_fields['avis_prod'].choices = avis_choices
        super(FilterProduitForm, self).__init__(**kwargs)


class SortProduitForm(forms.Form):
    SORT = (
        ('BESTSALES', "Meilleures ventes"),
        ('PRICEASC', "Du moins cher au plus cher"),
        ('PRICEDESC', "Du plus cher au moins cher"),
        ('RATING', "Avis client")
    )

    select_sort_prod = forms.ChoiceField(
        label="Trier par",
        choices=SORT,
        widget=forms.Select(
            attrs={
                'onChange': "this.parentNode.submit()",
                'class': "form-control"
            }
        )
    )


class SpecificationProduitForm(forms.Form):
    kle_spec_prod = forms.CharField(
        label="Nom du spécification",
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    valeur_spec_prod = forms.CharField(
        label="Valeur",
        widget=forms.Textarea(
            attrs={
                'cols': "40",
                'rows': "1",
                'class': "form-control",
                'style': "resize: none;"
            }
        )
    )
