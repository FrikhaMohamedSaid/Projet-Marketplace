from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import never_cache

from Dynamic_Champs.forms import PaysForm, CategorieForm, MarqueForm
from Dynamic_Champs.models import Pays, Categorie, Marque


@never_cache
@permission_required('is_superuser')
def create_pays(request):
    # Initialiser le formulaire du pays
    paysForm = PaysForm(
        data=request.POST or None
    )

    # Si le formulaire a été envoyer
    if request.method == "POST":
        if paysForm.is_valid():
            paysForm.save()

            return HttpResponseRedirect(
                reverse('R_Pays')
            )
    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Dynamic_Champs/C_U_Pays.html',
        {
            'form': paysForm
        }
    )


@never_cache
@permission_required('is_superuser')
def update_pays(request, pays_id):
    # recuperer le pays avec l'id 'pays_id'
    pays_obj = get_object_or_404(Pays, pk=pays_id)

    # Initialiser le formulaire du pays
    paysForm = PaysForm(
        data=request.POST or None,
        instance=pays_obj
    )

    # Si le formulaire a été envoyer
    if request.method == "POST":
        if paysForm.is_valid():
            paysForm.save()

            return HttpResponseRedirect(
                reverse('R_Pays')
            )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Dynamic_Champs/C_U_Pays.html',
        {
            'form': paysForm,
            'id': pays_id
        }
    )


@never_cache
@permission_required('is_superuser')
def read_pays(request):
    # Récuperer tous les pays du DB
    pays_list = Pays.objects.all()

    return render(
        request,
        'Dynamic_Champs/R_D_Pays.html',
        {
            'payss': pays_list
        }
    )


@never_cache
@permission_required('is_superuser')
def delete_pays(request, pays_id):
    get_object_or_404(Pays, pk=pays_id).delete()

    return HttpResponseRedirect(
        reverse('R_Pays')
    )


@permission_required('is_superuser')
def create_marque(request):
    # Initialiser le formulaire du marque
    marqueForm = MarqueForm(
        data=request.POST or None,
    )

    # Si le formulaire a été envoyer
    if request.method == "POST":
        if marqueForm.is_valid():
            marqueForm.save()

            return HttpResponseRedirect(
                reverse('R_Marque')
            )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Dynamic_Champs/C_U_Marque.html',
        {
            'form': marqueForm
        }
    )


@never_cache
@permission_required('is_superuser')
def update_marque(request, marque_id):
    marque_obj = get_object_or_404(Marque, pk=marque_id)

    # Initialiser le formulaire du marque
    marqueForm = MarqueForm(
        data=request.POST or None,
        instance= marque_obj
    )

    # Si le formulaire a été envoyer
    if request.method == "POST":
        if marqueForm.is_valid():
            marqueForm.save()

            return HttpResponseRedirect(
                reverse('R_Marque')
            )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Dynamic_Champs/C_U_Marque.html',
        {
            'form': marqueForm,
            'id': marque_id
        }
    )


@never_cache
@permission_required('is_superuser')
def read_marque(request):
    # Récuperer tous les marques du DB
    marque_list = Marque.objects.all()

    return render(
        request,
        'Dynamic_Champs/R_D_Marque.html',
        {
            'marques': marque_list
        }
    )


@never_cache
@permission_required('is_superuser')
def delete_marque(request, marque_id):
    get_object_or_404(Marque, pk=marque_id).delete()

    return HttpResponseRedirect(
        reverse('R_Marque')
    )


@never_cache
@permission_required('is_superuser')
def create_categorie(request):
    # Initialiser le formulaire du categorie
    categorieForm = CategorieForm(
        data=request.POST or None
    )

    # Si le formulaire a été envoyer
    if request.method == "POST":
        if categorieForm.is_valid():
            categorieForm.save()

            return HttpResponseRedirect(
                reverse('R_Categorie')
            )
    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Dynamic_Champs/C_U_Categorie.html',
        {
            'form': categorieForm
        }
    )


@never_cache
@permission_required('is_superuser')
def update_categorie(request, categ_id):
    # recuperer le categorie avec l'id 'categ_id'
    categ_obj = get_object_or_404(Categorie, pk=categ_id)

    # Initialiser le formulaire du categorie
    categorieForm = CategorieForm(
        data=request.POST or None,
        instance=categ_obj
    )

    # Si le formulaire a été envoyer
    if request.method == "POST":
        if categorieForm.is_valid():
            categorieForm.save()

            return HttpResponseRedirect(
                reverse('R_Categorie')
            )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Dynamic_Champs/C_U_Categorie.html',
        {
            'form': categorieForm,
            'id': categ_id
        }
    )


@never_cache
@permission_required('is_superuser')
def read_categorie(request):
    # Récuperer tous les categories du DB
    categ_list = Categorie.objects.all()

    return render(
        request,
        'Dynamic_Champs/R_D_Categorie.html',
        {
            'categories': categ_list
        }
    )


@never_cache
@permission_required('is_superuser')
def delete_categorie(request, categ_id):
    get_object_or_404(Categorie, pk=categ_id).delete()

    return HttpResponseRedirect(
        reverse('R_Categorie')
    )