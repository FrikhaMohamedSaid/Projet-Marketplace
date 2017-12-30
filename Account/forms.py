from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from Acheteur.models import Acheteur
from Vendeur.models import Vendeur


class AcheteurInscriptionForm(forms.ModelForm):
    re_password = forms.CharField(
        label="Confirmer votre mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        ),
    )

    class Meta:
        model = Acheteur
        fields = [
            'last_name',
            'first_name',
            'email',
            'username',
            'password',
            're_password',
        ]
        labels = {
            'last_name': "Nom",
            'first_name': "Prénom",
            'email': "E-Mail",
            'username': "Pseudo",
            'password': "Mot de passe",
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
            'password': forms.PasswordInput(
                attrs={
                    'class': "form-control"
                }
            )
        }

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password and re_password and password != re_password:
            raise forms.ValidationError("Les deux mot de passe ne sont pas identiques")
        return re_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            password_validation.validate_password(self.cleaned_data.get('password'), self.instance)
        return password


class VendeurCreateForm(forms.ModelForm):
    class Meta:
        model = Vendeur
        fields = [
            'last_name',
            'first_name',
            'email',
            'registre_commerce_bout'
        ]
        labels = {
            'last_name': "Nom",
            'first_name': "Prénom",
            'email': "E-Mail",
            'registre_commerce_bout': "Code de Registre de Commerce"
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
            'registre_commerce_bout': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            )
        }


class PasswordUpdateForm(forms.ModelForm):
    old_password = forms.CharField(
        label="Ancient mot de passe",
        widget=forms.PasswordInput(
            attrs=
            {
                'class': "form-control"
            }
        ),
    )
    renew_password = forms.CharField(
        label="Confirmer le nouveau mot de passe",
        help_text="Saisissez le même mot de passe que précédemment, pour vérification.",
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'old_password',
            'password',
            'renew_password',
        ]
        labels = {
            'password': "Nouveau mot de passe",
        }
        widgets = {
            'password': forms.PasswordInput(
                attrs={
                    'class': "form-control"
                }
            )
        }

    def __init__(self, user, data, **kwargs):
        self.user = user
        super(PasswordUpdateForm, self).__init__(data, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if old_password and not self.user.check_password(old_password):
            raise forms.ValidationError("Ancien mot de passe incorrecte")
        return old_password

    def clean_renew_password(self):
        password = self.cleaned_data.get('password')
        renew_password = self.cleaned_data.get('renew_password')
        if password and renew_password and password != renew_password:
            raise forms.ValidationError("Les deux mot de passe ne sont pas identiques")
        return renew_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            password_validation.validate_password(self.cleaned_data.get('password'), self.instance)
        return password


class EtatDemandeForm(forms.Form):
    ETAT = (
        ('0', "En Cour..."),
        ('1', "Accepter"),
        ('-1', "Refuser")
    )

    etat_demande = forms.ChoiceField(
        choices=ETAT,
        widget=forms.Select(
            attrs={
                'class': "form-control"
            }
        )
    )
