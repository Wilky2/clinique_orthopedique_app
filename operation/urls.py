from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home_operation'),
    path('enregistrer_operation/',views.EnregistrerOperation.as_view(),name='enregistrer_operation'),
    path('lister_operation/',views.ListerOperation.as_view(),name='lister_operation'),
]