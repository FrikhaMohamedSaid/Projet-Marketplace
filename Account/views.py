from random import randint

from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import never_cache

from Account.forms import PasswordUpdateForm, AcheteurInscriptionForm, VendeurCreateForm, EtatDemandeForm
from Vendeur.models import Vendeur

userCreateForm = AcheteurInscriptionForm()
vendeurCreateForm = VendeurCreateForm()


@never_cache
def connexion(request):
    # Iitialiser le formulaire par default de Django d'authentification
    authenticationForm = AuthenticationForm(
        data=request.POST or None
    )

    # Personaliser le champs 'username' du formulaire
    authenticationForm.fields['username'].widget.attrs['class'] = "form-control"
    authenticationForm.fields['username'].widget.attrs['placeholder'] = _("username")

    # Personaliser le champs 'password' du formulaire
    authenticationForm.fields['password'].widget.attrs['class'] = "form-control"
    # authenticationForm.fields['password'].widget.attrs['onpaste'] = "return false;"
    authenticationForm.fields['password'].widget.attrs['placeholder'] = _("Password")

    if request.method == 'POST':
        if authenticationForm.is_valid():
            # Esseyer d'authentifier l'utilisateur avec les données saisies
            user = authenticate(request, **authenticationForm.cleaned_data)

            # s'il l'utilisateur est authentifier avec succée
            if user is not None:
                login(request, user)
                if request.POST.get('next') == '':
                    if user.is_superuser:
                        return HttpResponseRedirect(
                            reverse('accueil_admin')
                        )
                    else:
                        try:
                            user.acheteur.id
                            return HttpResponseRedirect(
                                reverse('U_Profil_Acheteur')
                            )
                        except:
                            return HttpResponseRedirect(
                                reverse('U_Profil_Vendeur')
                            )
                else:
                    return HttpResponseRedirect(
                        request.POST.get('next')
                    )
            else:
                return HttpResponse("Probléme Serveur")

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Account/Connexion.html',
        {
            'form': authenticationForm
        }
    )


@never_cache
def inscription_acheteur(request):
    global userCreateForm

    # initialiser le formulaire d'inscription
    userCreateForm = AcheteurInscriptionForm(
        data=request.POST or None
    )

    # Si le formulaire a été envoyer
    if request.method == 'POST':
        if userCreateForm.is_valid():
            # préparer l'objet Acheteur
            new_user_obj = userCreateForm.save(commit=False)
            # Crypter le mot de passe
            new_user_obj.set_password(new_user_obj.password)
            # Ajouter dans la base
            new_user_obj.save()

            # Redirection vers la page d'authentification
            return HttpResponseRedirect(
                reverse('Connexion')
            )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Account/Inscription.html',
        {
            'acheteur_form': userCreateForm,
            'vendeur_form': vendeurCreateForm
        }
    )


@never_cache
def inscription_vendeur(request):
    # global vendeurCreateForm

    # initialiser le formulaire d'inscription
    vendeurCreateForm = VendeurCreateForm(
        data=request.POST or None
    )

    # Si le formulaire a été envoyer
    if request.method == 'POST':
        if vendeurCreateForm.is_valid():
            # préparer l'objet Vendeur
            new_vendeur_obj = vendeurCreateForm.save(commit=False)
            new_vendeur_obj.is_active = False
            # generer un nouveau username
            new_vendeur_obj.username = new_vendeur_obj.last_name + '_' + str(randint(0, 999999))
            # Ajouter dans la base
            new_vendeur_obj.save()

            return render(
                request,
                'Account/redirection.html'
            )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Account/Inscription.html',
        {
            'form': vendeurCreateForm
        }
    )


@login_required
@never_cache
def update_Password(request):
    # recuperer l'utilisateur avec l'id 'user_id'
    user_obj = get_object_or_404(User, pk=request.user.id)

    # Initialiser le formulaire de password
    password_form = PasswordUpdateForm(
        data=request.POST or None,
        instance=user_obj,
        user=user_obj
    )

    # Si l'utilisateur à changer le password
    if request.method == 'POST':
        if password_form.is_valid():
            baseModelPassword = password_form.save(commit=False)
            # Crypter le password avec le systeme definit dans le fichier setting
            baseModelPassword.set_password(baseModelPassword.password)
            baseModelPassword.save()

            # Mettre ajour la session
            update_session_auth_hash(request, password_form.user)

            try:
                request.user.acheteur.id
                return HttpResponseRedirect(
                    reverse('U_Profil_Acheteur')
                )
            except:
                return HttpResponseRedirect(
                    reverse('U_Profil_Vendeur')
                )

    # Si pas de formulaire envoyer / si le formulaire n'est pas valide
    return render(
        request,
        'Account/U_Password.html',
        {
            'form': password_form,
            'user_pass': user_obj
        }
    )


@permission_required('is_superuser')
def demande_vendeur(request):
    # Recupeter tous les demandes (compte inactif et pas de password)
    demande_list = Vendeur.objects.filter(
        is_active=False,
        password__exact=''
    )

    # Definir les multi forms d'etat des demandes
    formset = formset_factory(
        form=EtatDemandeForm,
        extra=0
    )

    # si le formulaire a été envoyer
    if request.method == 'POST':
        # initiliser les valeurs des forms
        etat_demande_formset = formset(
            data=request.POST or None,
        )

        if etat_demande_formset.is_valid():
            # parcourir chaque formulaire dans le formset
            i = 0
            for form in etat_demande_formset:
                # for i, form in enumerate(etat_demande_formset, start=0):
                etat_demande_user = form.cleaned_data['etat_demande']

                # Accepter
                if (etat_demande_user == "1"):
                    # generer un nouveau password
                    new_password = demande_list[i].first_name + str(randint(0, 999999))

                    # preparation de l'objet du vendeur avec le nouveau username et activation du compte
                    vendeur_obj = Vendeur(
                        pk=demande_list[i].id,
                        is_active=True
                    )

                    # cryptage du mot de passe
                    vendeur_obj.set_password(new_password)

                    # sauvgarder les nouvelle parametres
                    vendeur_obj.save(
                        force_update=True,
                        update_fields=[
                            'is_active',
                            'password'
                        ]
                    )

                    # recuperer l'email du vendeur juste modifier
                    vendeur_obj = Vendeur.objects.get(pk=vendeur_obj.id)

                    # appel au page html
                    html_content = get_template(
                        'Account/email.html'
                    )

                    # render page avec les données passer en dict
                    html_render = html_content.render(
                        {
                            'new_username': vendeur_obj.username,
                            'new_password': new_password
                        }
                    )

                    # preparation de l'email (objet, page html, de, list to)
                    msg = EmailMultiAlternatives(
                        'Acceptation Demande Compte MarquetPlace',
                        html_render,
                        'MarketPlace Admin',
                        [vendeur_obj.email]
                    )

                    # definir type contenu attaché
                    msg.content_subtype = "html"

                    # envoie du l'email
                    msg.send()

                # Refuser
                elif (etat_demande_user == "-1"):

                    # recuperation du vendeur
                    user_obj = get_object_or_404(
                        Vendeur,
                        pk=demande_list[i].id
                    )

                    # envoie d'un simple email
                    send_mail(
                        "Refus Demande Compte MarquetPlace",
                        "Votre demande d'inscription dans notre Marquetplace a été refuser.",
                        "MarketPlace Admin",
                        [user_obj.email]
                    )

                    # supprimer l'inscription du vendeur
                    user_obj.delete()
                else:
                    i += 1

    else:
        # initiliser les valeurs des forms
        etat_demande_formset = formset(
            initial=demande_list
        )

    # ziper les listes des demandes avec le formset
    zipped = zip(demande_list, etat_demande_formset)

    return render(
        request,
        'Account/Vendeur_Demandes.html',
        {
            'formset': etat_demande_formset,
            'zipped': zipped
        }
    )
