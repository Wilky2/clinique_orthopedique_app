from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home_hospitalisation'),
    path('enregistrer_hospitalisation/',views.EnregistrerHospitalisation.as_view(),name='enregistrer_hospitalisation'),
    path('liste_hospitalisation/',views.ListerHospitalisation.as_view(),name="liste_hospitalisation"),
    path('modifier_hospitalisation/<int:id>',views.ModifierHospitalisation.as_view(),name='modifier_hospitalisation'),
]