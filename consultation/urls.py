from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home_consultation'),
    path('enregistrer_consultation/',views.EnregistrerConsultation.as_view(),name='enregistrer_consultation'),
    path('enregistrer_dossier/',views.EnregistrerDossier.as_view(),name='enregistrer_dossier'),
    path('lister_consultation/',views.ListerConsultation.as_view(),name='lister_consultation'),
    path('lister_dossier/',views.ListerDossier.as_view(),name='lister_dossier'),
]