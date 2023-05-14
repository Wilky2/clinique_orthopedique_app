"""clinique_orthopedique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import accueil
import comptabilite
import consultation
import hospitalisation
import imagerie_medicale
import operation
import authentication
from authentication.views import DefaultHome
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',DefaultHome.as_view(),name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accueil/',include("accueil.urls")),
    path('comptabilite/',include("comptabilite.urls")),
    path('consultation/',include("consultation.urls")),
    path('hospitalisation/',include("hospitalisation.urls")),
    path('imagerie_medicale/',include("imagerie_medicale.urls")),
    path('operation/',include("operation.urls")),
    path('authentication/',include("authentication.urls")),
]
