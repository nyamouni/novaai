from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('etre_contacter.html', views.etre_contacter, name='etre_contacter'),
    path('service-details.html', views.details, name='details'),
    path('envoyer_message/', views.envoyer_message, name='envoyer_message'),
]
