from django.contrib.auth.decorators import user_passes_test
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

from Account.permission import is_acheteur
from Relation_Acheteur_Article.forms import PanierForm
from Relation_Acheteur_Article.models import Produit_Favori, Panier, Avis


@never_cache
@user_passes_test(is_acheteur)
def add_favori(request):
    # recuperer le parametre envoyer par ajax
    produit_id = request.GET['produit_id']
    # crée un objet avec ces parametres s'il n'existe pas
    produit_favori_obj, created = Produit_Favori.objects.get_or_create(
        acheteur_fav_id_id=request.user.acheteur.id,
        produit_fav_id_id=produit_id
    )

    # nouveau favori
    if created:
        return JsonResponse({'created': True})
    # favori existe deja
    else:
        produit_favori_obj.delete()
        return JsonResponse({'created': False})


@never_cache
@user_passes_test(is_acheteur)
def read_favori(request):
    # recuprer les favoris du acheteur connecter
    produit_Favori_user_list = Produit_Favori.objects.filter(
        acheteur_fav_id_id=request.user.acheteur.id
    )

    return render(
        request,
        'Relation_Acheteur_Article/R_D_Favori.html',
        {
            'favoris_user': produit_Favori_user_list
        }
    )


@never_cache
@user_passes_test(is_acheteur)
def delete_favori(request, favori_id):
    get_object_or_404(Produit_Favori, pk=favori_id).delete()

    return HttpResponseRedirect(
        reverse('R_Favori')
    )


@never_cache
@user_passes_test(is_acheteur)
def update_panier(request, produit_id):
    # creer un objet panier avec ces parametres s'il n'existe pas
    panier_obj, created = Panier.objects.get_or_create(
        acheteur_panier_id_id=request.user.acheteur.id,
        produit_panier_id_id=produit_id,
    )

    # initialiser la quantité à 1 pour les nouveaux object dans panier
    # sinon augmenter par 1 la quantité des anciens objets
    panier_obj.quantite_prod_panier += 1
    panier_obj.save()

    return HttpResponseRedirect(
        reverse('R_Panier')
    )



@never_cache
@user_passes_test(is_acheteur)
def read_panier(request):
    # recuperer tous les lignes de panier correspond à acheteur connecter
    panier_user_list = Panier.objects.filter(
        acheteur_panier_id_id=request.user.acheteur.id
    )

    total_panier = 0
    total_item_list = []
    for panier_user in panier_user_list:
        total_item = ((panier_user.produit_panier_id.prix_original_prod * panier_user.quantite_prod_panier) *
                      (100 - panier_user.produit_panier_id.pourcentage_solde_prod)
                      ) / 100
        total_panier += total_item
        total_item_list.append(total_item)

    ArticleFormSet = modelformset_factory(
        Panier,
        form=PanierForm,
        extra=0,
    )

    if request.method == 'POST':
        panier_formset = ArticleFormSet(
            data=request.POST or None,
        )

        if panier_formset.is_valid():
            panier_formset.save()
    else:
        panier_formset = ArticleFormSet(
            queryset=panier_user_list
        )

    zipped = zip(
        panier_user_list,
        total_item_list,
        panier_formset
    )

    return render(
        request,
        'Relation_Acheteur_Article/R_D_Panier.html',
        {
            'zipped': zipped,
            'formset': panier_formset,
            'total_panier': total_panier
        }
    )


@never_cache
@user_passes_test(is_acheteur)
def delete_panier(request, panier_id):
    get_object_or_404(
        Panier,
        pk=panier_id,
        acheteur_panier_id=request.user.acheteur.id
    ).delete()

    return HttpResponseRedirect(
        reverse('R_Panier')
    )


@never_cache
@user_passes_test(is_acheteur)
def add_update_avis(request, produit_id):
    if request.method == 'POST':
        # crée un objet avec l'id du acheteur et id du produit s'il n'existe pas
        # sinon modifier l'avis avec la note et commantaire saisie
        avis_obj, created = Avis.objects.update_or_create(
            acheteur_avis_id_id=request.user.acheteur.id,
            produit_avis_id_id=produit_id,
            defaults={
                'note_avis': request.POST['note_avis'],
                'commantaire_avis': request.POST['commantaire_avis']
            }
        )

        return redirect(request.META['HTTP_REFERER'])
        # # nouveau avis
        # if created:
        #     return JsonResponse({'created': True, 'new_avis_id': avis_obj.id})
        # # avis modifier
        # else:
        #     return JsonResponse({'created': False})


@never_cache
@user_passes_test(is_acheteur)
def delete_avis(request, avis_id):
    # avis_id = request.POST['avis_id']
    get_object_or_404(
        Avis,
        pk=avis_id,
        acheteur_avis_id=request.user.acheteur.id
    ).delete()

    return redirect(request.META['HTTP_REFERER'])
    # return JsonResponse({'delete': True})
