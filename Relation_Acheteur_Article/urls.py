from django.conf.urls import url

from Relation_Acheteur_Article import views

urlpatterns = [
    url(r'^favori/add', views.add_favori, name='Add_Favori'),
    # url(r'^favori/(?P<produit_id>([0-9]+))/add', views.add_favori, name='Add_Favori'),
    url(r'^favori/read', views.read_favori, name='R_Favori'),
    url(r'^favori/(?P<favori_id>([0-9]+))/delete', views.delete_favori, name='D_Favori'),

    url(r'^panier/(?P<produit_id>([0-9]+))/add', views.update_panier, name='Add_Panier'),
    url(r'^panier/read', views.read_panier, name='R_Panier'),
    url(r'^panier/(?P<panier_id>([0-9]+))/delete', views.delete_panier, name='D_Panier'),

    # url(r'^avis/add', views.add_update_avis, name='Add_U_Avis'),
    url(r'^avis/(?P<produit_id>([0-9]+))/add', views.add_update_avis, name='Add_U_Avis'),
    url(r'^avis/(?P<avis_id>([0-9]+))/delete', views.delete_avis, name='D_Avis'),
    # url(r'^avis/delete', views.delete_avis, name='D_Avis'),
]