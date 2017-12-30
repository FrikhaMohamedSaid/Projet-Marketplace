from django.conf.urls import url
from django.contrib.auth.views import logout

from Account import views

urlpatterns = [
    url(r'^login', views.connexion, name='Connexion'),
    url(r'^logout$', logout, {'next_page': '/index/'}, name='Deconnexion'),

    url(r'^clien_compte', views.inscription_acheteur, name='AcheteurInscri'),
    url(r'^vendeur_compte', views.inscription_vendeur, name='VendeurInscri'),

    url(r'^password/update', views.update_Password, name='U_MDP'),

    url(r'^demande/read', views.demande_vendeur, name='R_Demande_Vendeur'),
]