from django import forms

from Relation_Acheteur_Article.models import Panier, Avis


class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = [
            'acheteur_panier_id',
            'produit_panier_id',
            'quantite_prod_panier'
        ]
        labels = {
            'quantite_prod_panier': "Quantité"
        }
        widgets = {
            'quantite_prod_panier': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'onchange': "this.form.submit()",
                    'pattern': "[0-9]{2}"
                }
            ),
            'acheteur_panier_id': forms.HiddenInput(),
            'produit_panier_id': forms.HiddenInput()
        }


class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = [
            'note_avis',
            'commantaire_avis'
        ]
        labels = {
            'note_avis': "Note",
            'commantaire_avis': "Commantaire"
        }
        widgets = {
            'commantaire_avis': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "6"
                }
            ),
            'note_avis': forms.NumberInput(
                attrs={
                    'type': "range",
                    'orient': "vertical",
                    'min': "0",
                    'max': "5",
                    'class': "form-control"
                }
            )
        }
