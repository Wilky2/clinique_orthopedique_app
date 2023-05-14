from django.db import models
from django.contrib.auth.models import AbstractUser
from medecin import models as mmodels

class User(AbstractUser):

    ACCUEIL = 'ACCUEIL'
    COMPTABILITE = 'COMPTABILITE'
    CONSULTATION = 'CONSULTATION'
    HOSPITALISATION = 'HOSPITALISATION'
    IMAGERIE_MEDICALE = 'IMAGERIE_MEDICALE'
    OPERATION = 'OPERATION'

    SERVICE_CHOICES = (
        (ACCUEIL,'ACCUEIL'),
        (COMPTABILITE,'COMPTABILITE'),
        (CONSULTATION,'CONSULTATION'),
        (HOSPITALISATION,'HOSPITALISATION'),
        (IMAGERIE_MEDICALE,'IMAGERIE_MEDICALE'),
        (OPERATION,'OPERATION'),
    ) 

    service = models.CharField(max_length=30, choices=SERVICE_CHOICES)



