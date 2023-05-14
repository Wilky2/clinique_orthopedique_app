from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home_accueil'),
    path('enregistrer_patient/',views.EnregistrerPatient.as_view(),name='enregistrer_patient'),
    path('enregistrer_responsable/<int:num_patient>',views.EnregistrerResponsable.as_view(),name='enregistrer_responsable'),
    path('enregistrer_visite/',views.EnregistrerVisite.as_view(),name='enregistrer_visite'),
    path('liste_patient/',views.ListePatient.as_view(),name='liste_patient'),
    path('liste_responsable/<int:num_patient>',views.ListeResponsable.as_view(),name='liste_patient'),
    path('liste_visite/',views.ListeVisite.as_view(),name='liste_visite'),
    path('modifier_patient/<int:id>',views.ModifierPatient.as_view(),name="modifier_patient"),
    path('choix_patient/',views.ChoixPatient.as_view(),name='choix_patient'),
    path('modifier_responsable/<int:id>',views.ModifierResponsable.as_view(),name="modifier_responsable"),
    path('choix_responsable/',views.ChoixResponsable.as_view(),name='choix_responsable'),
]
