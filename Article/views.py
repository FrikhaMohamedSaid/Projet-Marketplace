import ast
import operator
from functools import reduce

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Avg, Q
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import never_cache

from Account.permission import is_vendeur
from Article.forms import ProduitForm, FilterProduitForm, SortProduitForm, SpecificationProduitForm
from Article.models import Produit, Specification_Produit
from Dynamic_Champs.models import Marque, Categorie
from Relation_Acheteur_Article.forms import AvisForm
from Relation_Acheteur_Article.models import Avis
from Vendeur.models import Boutique

# GLOBAL VARIABLE (declaration et initialisation)
etat_filter = []

produit_list_filtred = produit_list = Produit.objects.all()

marque_filter = Marque.objects.all()

categorie_filter = Categorie.objects.all()

sortProduitForm = SortProduitForm()

filterProduitForm = FilterProduitForm(
    initial={
        'prix_min_prod': 0
    }
)

for x, y in Produit.ETAT:
    etat_filter.append(x)


# FUNCTIONS

@never_cache
@user_passes_test(is_vendeur)
def create_produit(request):
    # formulaire du produit simple
    produitForm = ProduitForm(
        data=request.POST or None,
        files=request.FILES or None
    )

    # formualire multiple
    SpecificationFormSet = formset_factory(
        # pointe sur le formuaire simple
        form=SpecificationProduitForm,
        # possibiliter de supppression des champs
        can_delete=True,
        # initiale 1
        extra=1,
    )

    # initialisation du formulaire avec les données en POST sinon vide
    specificationFormSet = SpecificationFormSet(
        data=request.POST or None
    )

    if request.method == 'POST':
        if produitForm.is_valid() and specificationFormSet.is_valid():

            new_produit_obj = produitForm.save(commit=False)
            new_produit_obj.boutique_prod_id = Boutique.objects.get(vendeur_bout_id_id=request.user.id)
            new_produit_obj.save()

            # si il y a une modification dans le formset
            if specificationFormSet.has_changed():

                list_specification = {}

                for form in specificationFormSet:
                    # si le bouton supprimer n'est pas cochet et le champs de velur n'est pas vide
                    if (not form.cleaned_data.get('DELETE')) and (form.cleaned_data.get('valeur_spec_prod') is not None):
                        list_specification[form.cleaned_data['kle_spec_prod']] = form.cleaned_data['valeur_spec_prod']

                # save()
                Specification_Produit.objects.create(
                    kle_value_spec_prod=list_specification,
                    produit_spec_prod=new_produit_obj
                )

            return HttpResponseRedirect(
                reverse('R_Vendeur_Produit')
            )

    return render(
        request,
        'Article/C_U_Produit.html',
        {
            'form': produitForm,
            'formset': specificationFormSet
        }
    )


@never_cache
@user_passes_test(is_vendeur)
def update_produit(request, produit_id):
    produit_obj = get_object_or_404(Produit, pk=produit_id)

    # formulaire du produit simple
    produitForm = ProduitForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=produit_obj
    )

    # formualire multiple
    SpecificationFormSet = formset_factory(
        # pointe sur le formuaire simple
        form=SpecificationProduitForm,
        # possibiliter de supppression des champs
        can_delete=True,
        # initiale 0
        extra=0,
    )

    # recuperer s'il existe la ligne de specification du base correspondante a ce produit
    # (filter ne genere pas d'erreur)
    # puisque c'est toujour une seul ligne donc on lit la premiaire ligne
    specification_obj = Specification_Produit.objects.filter(
        produit_spec_prod=produit_obj,
    ).first()

    # declaration du liste dinitialisation du formset
    initial_specificationFormSet = []

    # s'il existe une ligne de specification
    if specification_obj is not None:
        # convertir le string enregistrer dans 'kle_value_spec_prod' à dict
        kle_value_dict = ast.literal_eval(specification_obj.kle_value_spec_prod)

        for key, value in kle_value_dict.items():
            item_specificationForm = {}
            item_specificationForm['kle_spec_prod'] = key
            item_specificationForm['valeur_spec_prod'] = value
            initial_specificationFormSet.append(item_specificationForm)

    # initialisation du formulaire
    specificationFormSet = SpecificationFormSet(
        data=request.POST or None,
        initial=initial_specificationFormSet
    )

    # si les formulaires ont envoyé
    if request.method == 'POST':
        if produitForm.is_valid() and specificationFormSet.is_valid():
            produitForm.save()

            # si il y a une modification dans le formset
            if specificationFormSet.has_changed():

                list_specification = {}

                for form in specificationFormSet:
                    # si le bouton supprimer n'est pas cochet et le champs de velur n'est pas vide
                    if (not form.cleaned_data.get('DELETE')) and (form.cleaned_data.get('valeur_spec_prod') is not None):
                        list_specification[form.cleaned_data['kle_spec_prod']] = form.cleaned_data['valeur_spec_prod']

                Specification_Produit.objects.update_or_create(
                    produit_spec_prod_id=produit_id,
                    defaults={
                        'kle_value_spec_prod': list_specification
                    }
                )

            return HttpResponseRedirect(
                reverse('R_Vendeur_Produit')
            )

    return render(
        request,
        'Article/C_U_Produit.html',
        {
            'form': produitForm,
            'id': produit_id,
            'formset': specificationFormSet
        }
    )


@never_cache
@user_passes_test(is_vendeur)
def delete_produit(request, produit_id):
    get_object_or_404(Produit, pk=produit_id).delete()

    return HttpResponseRedirect(
        reverse('R_Vendeur_Produit')
    )


def vendre_produit(request, produit_id, quantite_vendue):
    produit_obj = get_object_or_404(Produit, pk=produit_id)
    produit_obj.quantite_vendue_prod += quantite_vendue
    produit_obj.save()


@never_cache
def read_one_produit(request, produit_id):
    # recuperer le produit avec l'id produit_id
    produit_obj = get_object_or_404(Produit, pk=produit_id)

    # reccuprer les avis associer à ce produit
    avis_obj = Avis.objects.filter(
        produit_avis_id=produit_obj
    )

    specifications_dict = {}

    try:
        # recuperer s'il existe la ligne de specification du base correspondante a ce produit
        specification_obj = Specification_Produit.objects.get(produit_spec_prod=produit_obj)
        specifications_dict = ast.literal_eval(specification_obj.kle_value_spec_prod)
    except:
        pass

    # initialiser le formulaire de l'avis avec les données saisie par l'acheteur connecter sinon vide
    avisForm = AvisForm(
        data=request.POST or None,
        instance=avis_obj.filter(
            acheteur_avis_id_id=request.user.id
        ).first()
    )

    return render(
        request,
        'Article/R_One_Produit.html',
        {
            'produit': produit_obj,
            'aviss': avis_obj,
            'form': avisForm,
            'specifications': specifications_dict
        }
    )


def read_all_produit(request):
    # appel des varibales globales pour les modifiers
    global produit_list_filtred, produit_list, filterProduitForm

    filterProduitForm = FilterProduitForm(
        initial={
            'prix_min_prod': 0
        }
    )

    # reinsaliser les deux variable de liste par les produits du bases (en cas de changement dans la base)
    produit_list_filtred = produit_list = Produit.objects.all()

    return render(
        request,
        'Article/R_All_Produit.html',
        {
            'produits': produit_list,
            'filterForm': filterProduitForm,
            'sortForm': sortProduitForm
        }
    )


@never_cache
@user_passes_test(is_vendeur)
def read_vendeur_produit(request):
    # recuperer les produits du vendeur connecter
    produit_list = Produit.objects.filter(
        boutique_prod_id__vendeur_bout_id_id=request.user.vendeur.id
    )

    return render(
        request,
        'Article/R_Vendeur_Produit.html',
        {
            'produits': produit_list,
        }
    )


def filter_list_produit_by_name(request):
    # appel des varibales globales pour les modifiers
    global produit_list_filtred

    # liste des mots saisies
    list_mots = []

    # couper le text saisie par les espaces
    for s_t in request.GET['search_text'].split(" "):
        # ajouter le mot au liste
        list_mots.append(s_t)

    # filter la liste des produits par:
    produit_list_filtred = produit_list.filter(
        reduce(
            # opérateur OU
            operator.or_, (
                # titre contient un des mots du liste
                Q(titre_prod__icontains=mot) for mot in list_mots
            )
        )
    )

    return render(
        request,
        'Article/R_All_Produit.html',
        {
            'produits': produit_list_filtred,
            'filterForm': filterProduitForm,
            'sortForm': sortProduitForm
        }
    )


def filter_list_produit_by_bar(request):
    # appel des varibales globales pour les modifiers
    global produit_list_filtred, filterProduitForm

    # filter la liste des produits par:
    produit_list_filtred = produit_list.filter(
        # par catégorie selectioner sinon retourner tout
        categorie_prod_id__in=request.GET.get('categorie_prod') or categorie_filter,
        # par condition selectioner sinon retourner tout
        condition_prod__in=request.GET.getlist('condition_prod') or etat_filter,
        # par prix minimal selectioner par l'utilisateur
        prix_original_prod__gte=request.GET['prix_min_prod'],
        # par marque selectionner sinon retourner tout
        marque_prod_id__in=request.GET.getlist('marque_prod') or marque_filter,
        # par avis selectioner sinon retourner tout
        note_avis_prod__range=(request.GET.get('avis_prod') or 0, 5)
    )

    # si l'utilisateur a selectioner un niveau d'avis
    if request.GET.get('avis_prod'):
        # recuperer juste cette avis
        NEW_AVIS = [FilterProduitForm.AVIS[int(request.GET.get('avis_prod')) - 1]]
    else:
        # recuperer tout les avis initiales
        NEW_AVIS = FilterProduitForm.AVIS

    # initialiser le formulaire avec les donnée envoyer par utilisateurs
    filterProduitForm = FilterProduitForm(
        data=request.GET or None,
        # modifier les chois d'avis
        avis_choices=NEW_AVIS
    )

    return render(
        request,
        'Article/R_All_Produit.html',
        {
            'produits': produit_list_filtred,
            'filterForm': filterProduitForm,
            'sortForm': sortProduitForm
        }
    )


def sort_list_produit(request):
    # appel des varibales globales pour les modifiers
    global sortProduitForm

    select_sort_value = request.GET['select_sort_prod']

    # initialiser le formulaire avec le choix du utilisateur
    sortProduitForm = SortProduitForm(
        data=request.GET or None
    )

    # si le choix "Meilleures ventes"
    if select_sort_value == "BESTSALES":
        # fonction de trie
        produit_list_sorted = sorted(
            # les produits filtrer
            produit_list_filtred,
            # selon le quantité vendue des produits
            key=operator.attrgetter('quantite_vendue_prod'),
            # Ordre decroissant
            reverse=True
        )

    # si le choix "Du moins cher au plus cher"
    elif select_sort_value == "PRICEASC":
        # fonction de trie
        produit_list_sorted = sorted(
            # les produits filtrer
            produit_list_filtred,
            # selon le prix original des produits
            key=operator.attrgetter('prix_original_prod'),
            # Ordre croissant
            reverse=False
        )

    # si le choix "Du plus cher au moins cher"
    elif select_sort_value == "PRICEDESC":
        # fonction de trie
        produit_list_sorted = sorted(
            # les produits filtrer
            produit_list_filtred,
            # selon le prix original des produits
            key=operator.attrgetter('prix_original_prod'),
            # ordre decroissant
            reverse=True
        )

    elif select_sort_value == "RATING":
        # fonction de trie
        produit_list_sorted = sorted(
            # les produits filtrer
            produit_list_filtred,
            # selon le note des avis des produits
            key=operator.attrgetter('note_avis_prod'),
            # ordre decroissant
            reverse=True
        )

    return render(
        request,
        'Article/R_All_Produit.html',
        {
            'produits': produit_list_sorted,
            'filterForm': filterProduitForm,
            'sortForm': sortProduitForm
        }
    )
