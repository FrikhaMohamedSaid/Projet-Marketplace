from django import forms
from django.http import HttpResponse

from Vendeur.models import Vendeur, Boutique


class VendeurProfilForm(forms.ModelForm):
    class Meta:
        model = Vendeur
        fields = [
            'last_name',
            'first_name',
            'email',
            'username',
        ]
        labels = {
            'last_name': "Nom",
            'first_name': "Prénom",
            'email': "E-Mail",
            'username': "Pseudo"
        }
        widgets = {
            'last_name': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'first_name': forms.TextInput(
                attrs={

                    'class': "form-control"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            )
        }


class BoutiqueForm(forms.ModelForm):
    class Meta:
        model = Boutique
        fields = [
            'nom_bout',
            'description_bout',
            'adresse_bout',
            'pays_bout_id',
            'logo_bout'
        ]
        labels = {
            'nom_bout': "Nom du Boutique",
            'description_bout': "A propos de votre boutique",
            'adresse_bout': "Adresse",
            'pays_bout_id': "Pays",
            'logo_bout': "Logo"
        }
        widgets = {
            'nom_bout': forms.TextInput(
                attrs={
                    'autocomplete': "off",
                    'class': "form-control"
                }
            ),
            'description_bout': forms.Textarea(
                attrs={
                    'class': "form-control"
                }
            ),
            'adresse_bout': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'pays_bout_id': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'logo_bout': forms.FileInput(
                attrs={
                    'accept': "image/*"
                }
            )
        }

    def __init__(self, **kwargs):
        try:
            if not kwargs['instance'].logo_bout:
                self.base_fields['logo_bout'].widget.attrs['required'] = ""
        except:
            pass

        super(BoutiqueForm, self).__init__(**kwargs)
