from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home_imagerie_medicale'),
    path('enregistrer_examen/',views.EnregistrerExamen.as_view(),name='enregistrer_examen'),
    path('enregistrer_prescription/',views.EnregistrerPrescription.as_view(),name='enregistrer_prescription'),
    path('enregistrer_rendez_vous/',views.EnregistrerRendezVous.as_view(),name='enregistrer_rendez_vous'),
    path('lister_examen/',views.ListerExamen.as_view(),name='lister_examen'),
    path('lister_prescription/',views.ListerPrescription.as_view(),name='lister_prescription'),
    path('lister_rendez_vous/',views.ListerRendezVous.as_view(),name='lister_rendez_vous'),
]