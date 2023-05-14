from django.db import models

from medecin import models as umodels

from accueil import models as acmodels

class Dossier(models.Model):
    num_dossier = models.AutoField(primary_key=True)
    etat_dossier = models.BooleanField(default=True)
    num_patient = models.OneToOneField(acmodels.Patient, on_delete=models.CASCADE)

class Consulter(models.Model):
    num_medecin = models.ForeignKey(umodels.Medecin,on_delete=models.CASCADE)
    num_patient = models.ForeignKey(acmodels.Patient,on_delete=models.CASCADE)
    date_consultation = models.DateTimeField(auto_now_add=True)
    tension_corporelle = models.FloatField()
    resultat_consultation = models.TextField()

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['num_patient','num_medecin','date_consultation'],name='patient_medecin_date_consultation_unique')
        ]
