from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


def index(request):
    return render(request, 'contactform/index.html')
def etre_contacter(request):
    return render(request, 'contactform/etre_contacter.html')
def details(request):
    return render(request, 'contactform/service-details.html')
def envoyer_message(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        sujet = request.POST.get('subject')

        contenu = f"Besoin de contact : Nom : {nom}\nEmail : {email}\n\nNumero :\n{sujet}"

        send_mail(
            sujet,
            contenu,
            settings.EMAIL_HOST_USER,  # expediteur
            [settings.EMAIL_HOST_USER],  # destinataire
            fail_silently=False,
        )

        messages.success(request, 'Votre message a été envoyé avec succès.')
        return redirect('etre_contacter')  # ou une autre page
    return redirect('etre_contacter')
