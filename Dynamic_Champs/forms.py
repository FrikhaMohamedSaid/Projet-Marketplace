from django import forms

from Dynamic_Champs.models import Pays, Categorie, Marque


class PaysForm(forms.ModelForm):
    class Meta:
        model = Pays
        fields = [
            'nom_pays'
        ]
        labels = {
            'nom_pays': "Nom du Pays"
        }
        widgets = {
            'nom_pays': forms.TextInput(
                attrs={
                    'autocomplete': "off",
                    'class': "form-control"
                }
            ),
        }


class MarqueForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields = [
            'nom_marque'
        ]
        labels = {
            'nom_marque': "Nom du marque"
        }
        widgets = {
            'nom_marque': forms.TextInput(
                attrs={
                    'autocomplete': "off",
                    'class': "form-control"
                }
            )
        }


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = [
            'nom_categ',
            'description_categ'
        ]
        labels = {
            'nom_categ': "Nom du Catégorie",
            'description_categ': "Description"
        }
        widgets = {
            'nom_categ': forms.TextInput(
                attrs={
                    'autocomplete': "off",
                    'class': "form-control"
                }
            ),
            'description_categ': forms.Textarea(
                attrs={
                    'class': "form-control"
                }
            )
        }