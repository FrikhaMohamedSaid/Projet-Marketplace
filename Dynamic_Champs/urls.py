from django.conf.urls import url

from Dynamic_Champs import views

urlpatterns = [
    url(r'^pays/create', views.create_pays, name='C_Pays'),
    url(r'^pays/(?P<pays_id>([0-9]+))/update', views.update_pays, name='U_Pays'),
    url(r'^pays/read', views.read_pays, name='R_Pays'),
    url(r'^pays/(?P<pays_id>([0-9]+))/delete', views.delete_pays, name='D_Pays'),

    url(r'^marque/create', views.create_marque, name='C_Marque'),
    url(r'^marque/(?P<marque_id>([0-9]+))/update', views.update_marque, name='U_Marque'),
    url(r'^marque/read', views.read_marque, name='R_Marque'),
    url(r'^marque/(?P<marque_id>([0-9]+))/delete', views.delete_marque, name='D_Marque'),

    url(r'^categorie/create', views.create_categorie, name='C_Categorie'),
    url(r'^categorie/(?P<categ_id>([0-9]+))/update', views.update_categorie, name='U_Categorie'),
    url(r'^categorie/read', views.read_categorie, name='R_Categorie'),
    url(r'^categorie/(?P<categ_id>([0-9]+))/delete', views.delete_categorie, name='D_Categorie'),
]