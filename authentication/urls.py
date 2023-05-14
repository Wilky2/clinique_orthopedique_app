from django.urls import path

from . import views

urlpatterns = [
    path('',views.Login.as_view(),name='login'),
    path('create_user/',views.CreateUser.as_view(),name='create_user'),
]