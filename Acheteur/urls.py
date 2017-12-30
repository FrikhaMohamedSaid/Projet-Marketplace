from django.conf.urls import url

from Acheteur import views

urlpatterns = [
    url(r'^profil/update', views.update_profil_acheteur, name='U_Profil_Acheteur'),
]