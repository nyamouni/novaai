"""
Le site a déménagé vers https://novaai-tech.com.

Ce module ne fait plus qu'une chose : renvoyer chaque visiteur — et chaque
robot d'indexation — vers la nouvelle adresse.

La réponse est un 301, « déplacé de façon permanente », et non un 302. C'est
ce qui indique à Google qu'il ne s'agit pas d'une absence passagère : il
transfère alors au nouveau domaine l'ancienneté et la réputation accumulées
ici, au lieu de le découvrir comme un inconnu. Tant que les deux sites
répondaient, ils se disputaient les mêmes recherches sur le même nom.

Le renvoi se fait en un seul saut : chaque ancienne page vise directement son
équivalent définitif. Une chaîne de redirections successives est suivie moins
volontiers par les robots, et perd en route une partie du bénéfice.
"""

from django.http import HttpResponsePermanentRedirect

NOUVEAU_SITE = "https://novaai-tech.com"

CORRESPONDANCES = {
    "/": "/",
    "/index.html": "/",
    "/etre_contacter.html": "/contact/",
    "/service-details.html": "/logiciels/",
    "/envoyer_message/": "/demander-un-devis/",
}

# Tout le reste — anciennes URL oubliées, liens erronés, exploration de robots —
# atterrit sur l'accueil plutôt que sur une erreur.
PAR_DEFAUT = "/"


class RedirigerVersLeNouveauSite:
    """
    Placée en tête de la pile, cette classe court-circuite tout le reste :
    ni vue, ni base de données, ni gabarit ne sont sollicités. Le renvoi
    fonctionne donc même si l'application ne démarre plus correctement.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        chemin = CORRESPONDANCES.get(request.path, PAR_DEFAUT)
        return HttpResponsePermanentRedirect(f"{NOUVEAU_SITE}{chemin}")
