from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import never_cache

from Account.permission import is_vendeur
from Traitement.compression import compression_size_photo
from Vendeur.forms import VendeurProfilForm, BoutiqueForm
from Vendeur.models import Vendeur, Boutique


@never_cache
@user_passes_test(is_vendeur)
def update_profil_vendeur(request):
    # recuperer les données du vendeur qui correspond à l'id passer en url
    vendeur_obj = get_object_or_404(Vendeur, pk=request.user.id)

    # recuperer les donners du formulaire sinon l'initialiser avec les donners du DB
    vendeurProfilForm = VendeurProfilForm(
        data=request.POST or None,
        instance=vendeur_obj
    )

    # si le formulaire a été envoyer
    if request.method == 'POST':
        if vendeurProfilForm.is_valid():
            vendeurProfilForm.save()


    # Sinon
    return render(
        request,
        'Vendeur/U_Profil_Vendeur.html',
        {
            'form': vendeurProfilForm,
            'id': request.user.id
        }
    )


@never_cache
@user_passes_test(is_vendeur)
def update_boutique(request):
    # si le boutique existe déja
    try:
        # récuperer les données du boutiques de celui connecter
        boutique_obj = get_object_or_404(Boutique, vendeur_bout_id_id=request.user.vendeur.id)
        # initiliser le formulaire avec ces données
        boutiqueForm = BoutiqueForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=boutique_obj
        )
    # Sinon
    except:
        # initiliser le formulaire
        boutiqueForm = BoutiqueForm(
            data=request.POST or None,
            files=request.FILES or None,
        )

    # si le formualire a été envoyer
    if request.method == 'POST':
        if boutiqueForm.is_valid():
            new_boutique_obj = boutiqueForm.save(commit=False)
            new_boutique_obj.vendeur_bout_id = Vendeur.objects.get(pk=request.user.vendeur.id)
            new_boutique_obj.save()

            # Compression du l'image logo (max_widh = max_height = 512px)
            compression_size_photo(src=new_boutique_obj.logo_bout, size=512)

            return HttpResponseRedirect(
                reverse(
                    'R_Boutique',
                    kwargs={
                        'boutique_id': new_boutique_obj.id
                    }
                )
            )

    # Sinon
    return render(
        request,
        'Vendeur/U_Boutique.html',
        {
            'form': boutiqueForm
        }
    )


@never_cache
def read_boutique(request, boutique_id=0):
    # afficher tous les boutiques
    if boutique_id == 0:
        # recuperer les informations des boutiques existantes
        boutique_list = Boutique.objects.all()

        return render(
            request,
            'Vendeur/R_All_Boutique.html',
            {
                'boutiques': boutique_list
            }
        )

    # afficher une seul boutique
    else:
        # recuperer les informations du boutique avec l'id la valeur 'boutique_id' passer en url
        boutique_obj = get_object_or_404(Boutique, pk=boutique_id)
        return render(
            request,
            'Vendeur/Profil_Boutique.html',
            {
                'boutique': boutique_obj
            }
        )


@never_cache
@user_passes_test(is_vendeur)
def delete_boutique(request, boutique_id):
    get_object_or_404(
        Boutique,
        pk=boutique_id,
        vendeur_bout_id=request.user.vendeur.id
    ).delete()

    return HttpResponse('ok')

