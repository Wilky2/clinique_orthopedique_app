from django.db import models

from medecin import models as umodels

from accueil import models as acmodels

class Prescription(models.Model):
    num_prescription = models.AutoField(primary_key=True)
    num_medecin = models.ForeignKey(umodels.Medecin,on_delete=models.CASCADE)
    num_patient = models.ForeignKey(acmodels.Patient,on_delete=models.CASCADE)
    description_prescription = models.TextField()

class Examiner(models.Model):
    num_medecin = models.ForeignKey(umodels.Medecin,on_delete=models.CASCADE)
    num_patient = models.ForeignKey(acmodels.Patient,on_delete=models.CASCADE)
    date_examen = models.DateTimeField(auto_now_add=True)
    type_examen = models.CharField(max_length=50)
    diagnostic_examen = models.TextField()

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['num_patient','num_medecin','date_examen'],name='patient_medecin_date_examen_unique')
        ]

class RendezVous(models.Model):
    num_rendez_vous = models.AutoField(primary_key=True)
    num_medecin = models.ForeignKey(umodels.Medecin,on_delete=models.CASCADE)
    num_patient = models.ForeignKey(acmodels.Patient,on_delete=models.CASCADE)
    date_rendez_vous = models.DateTimeField()