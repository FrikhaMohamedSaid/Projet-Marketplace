from django.conf.urls import url

from Vendeur import views

urlpatterns = [
    url(r'^profil/update', views.update_profil_vendeur, name='U_Profil_Vendeur'),

    url(r'^boutique/update', views.update_boutique, name='U_Boutique'),
    url(r'^boutique/all', views.read_boutique, name='R_All_Boutique'),
    url(r'^boutique/(?P<boutique_id>([0-9]+))/read', views.read_boutique, name='R_Boutique'),
    url(r'^boutique/(?P<boutique_id>([0-9]+))/delete', views.delete_boutique, name='D_Boutique'),
]