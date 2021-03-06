"""Marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^accounts/', include('Account.urls')),
    url(r'^dChamps/', include('Dynamic_Champs.urls')),
    url(r'^acheteur/', include('Acheteur.urls')),
    url(r'^vendeur/', include('Vendeur.urls')),
    url(r'^article/', include('Article.urls')),
    url(r'^rel_ach_art/', include('Relation_Acheteur_Article.urls')),

    url(r'^index/', views.Index, name='accueil'),
    url(r'^index_admin', views.IndexAmdin, name='accueil_admin'),
    url(r'^mail', views.mail, name=''),
    # url(r'^admin/', admin.site.urls),
    url(r'^', views.Index, name=''),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
