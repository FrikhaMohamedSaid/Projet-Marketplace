from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache

from Acheteur.forms import AcheteurProfilForm, AdresseForm
from Acheteur.models import Acheteur
from Account.permission import is_acheteur


@never_cache
@user_passes_test(is_acheteur)
def update_profil_acheteur(request):
    # recuperer les données du l'acheteur qui correspond à l'id passer en url
    acheteur_obj = get_object_or_404(Acheteur, pk=request.user.id)

    # recuperer les donners du formulaire sinon l'initialiser avec les donners du DB
    acheteurProfilForm = AcheteurProfilForm(
        data=request.POST or None,
        instance=acheteur_obj
    )
    adresseForm = AdresseForm(
        data=request.POST or None,
        instance=acheteur_obj.adresse_achet_id
    )

    # si le formulaire a été envoyer
    if request.method == 'POST':
        if acheteurProfilForm.is_valid() and adresseForm.is_valid():
            adresse_obj = adresseForm.save()
            new_acheteur_obj = acheteurProfilForm.save(commit=False)
            new_acheteur_obj.adresse_achet_id = adresse_obj
            new_acheteur_obj.save()


    # Sinon
    return render(
        request,
        'Acheteur/U_Profil_Acheteur.html',
        {
            'form': acheteurProfilForm,
            'adress_form': adresseForm,
            'id': request.user.id
        }
    )
