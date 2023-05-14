from django.db import models

from medecin import models as umodels

from accueil import models as acmodels

class Hospitaliser(models.Model):
    num_medecin = models.ForeignKey(umodels.Medecin,on_delete=models.CASCADE)
    num_patient = models.ForeignKey(acmodels.Patient,on_delete=models.CASCADE)
    date_debut_hospitalisation = models.DateTimeField(auto_now_add=True)
    date_fin_hospitalisation = models.DateTimeField(null=True,blank=True)

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['num_patient','num_medecin','date_debut_hospitalisation'],name='patient_medecin_date_debut_hospitalisation_unique')
        ]
