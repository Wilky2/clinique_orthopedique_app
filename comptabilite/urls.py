from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home_comptabilite'),
    path('enregistrer_paiement/',views.EnregistrerPaiement.as_view(),name='enregistrer_paiement'),
    path('enregistrer_carte_assurance/',views.EnregistrerCarteAssurance.as_view(),name='enregistrer_carte_assurance'),
    path('liste_paiement/',views.ListePaiement.as_view(),name='liste_paiement'),
    path('liste_carte_assurance/',views.ListeCarteAssurance.as_view(),name='liste_carte_assurance'),
    path('nombre_cheque/',views.NombreCheque.as_view(),name='nombre_cheque'),
    path('enregistrer_cheque/<int:quantite>',views.EnregistrerCheque.as_view(),name='enregistrer_cheque'),
    path('liste_cheque/',views.ListeCheque.as_view(),name='liste_cheque'),
    path('modifier_carte/<int:id>',views.ModifierCarteAssurance.as_view(),name="modifier_carte"),
]