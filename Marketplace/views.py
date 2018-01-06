from django.shortcuts import render

from Acheteur.models import Acheteur
from Article.models import Produit
from Vendeur.models import Boutique


def Index(request):
    statistique = {}

    boutique_list = Boutique.objects.all()
    acheteur_list = Acheteur.objects.all()
    produit_list = Produit.objects.all().order_by('-note_avis_prod')

    statistique['nbr_boutique'] = boutique_list.count()
    statistique['nbr_acheteur'] = acheteur_list.count()
    statistique['nbr_produit'] = produit_list.count()


    return render(
        request,
        'Base/index.html',
        {
            'boutiques': boutique_list,
            'produits': produit_list,
            'statistique': statistique
        }
    )


# @permission_required('is_superuser')
def IndexAmdin(request):
    return render(
        request,
        'BaseAdmin/index.html'
    )


def mail(request):
    return render(
        request,
        'Account/email.html'
    )