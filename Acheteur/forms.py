from django import forms

from Acheteur.models import Acheteur, Adresse


class AcheteurProfilForm(forms.ModelForm):
    class Meta:
        model = Acheteur
        fields = [
            'last_name',
            'first_name',
            'email',
            'username',
            'telephone_achet',
        ]
        labels = {
            'last_name': "Nom",
            'first_name': "Prénom",
            'email': "E-Mail",
            'username': "Pseudo",
            'telephone_achet': "N° de Téléphone",
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
            ),
            'telephone_achet': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            )
        }


class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = [
            'num_adr',
            'ville_adr',
            'code_postale_adr',
            'pays_adr'
        ]
        labels = {
            'num_adr': "N°",
            'ville_adr': "Adresse",
            'code_postale_adr': "Code Postale",
            'pays_adr': "Pays"
        }
        widgets = {
            'num_adr': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'ville_adr': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'code_postale_adr': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'pays_adr': forms.Select(
                attrs={
                    'class': "form-control"
                }
            )
        }
