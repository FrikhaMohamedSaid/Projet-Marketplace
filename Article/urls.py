from django.conf.urls import url

from Article import views

urlpatterns = [
    url(r'^produit/create', views.create_produit, name='C_Produit'),
    url(r'^produit/(?P<produit_id>([0-9]+))/update', views.update_produit, name='U_Produit'),
    url(r'^produit/(?P<produit_id>([0-9]+))/read', views.read_one_produit, name='R_One_Produit'),
    url(r'^produit/all', views.read_all_produit, name='R_All_Produit'),
    url(r'^produit/boutique/all', views.read_vendeur_produit, name='R_Vendeur_Produit'),
    url(r'^produit/(?P<produit_id>([0-9]+))/delete', views.delete_produit, name='D_Produit'),

    url(r'^produit/filter/(?:header_bar=true)', views.filter_list_produit_by_name, name='F_Produit_Name'),
    url(r'^produit/filter/(?:filter_bar=true)', views.filter_list_produit_by_bar, name='F_Produit_Bar'),
    url(r'^produit/sort', views.sort_list_produit, name='Sort_Produit'),
]