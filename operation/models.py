from django.db import models

from medecin import models as umodels

from accueil import models as acmodels

class Operer(models.Model):
    num_medecin = models.ForeignKey(umodels.Medecin,on_delete=models.CASCADE)
    num_patient = models.ForeignKey(acmodels.Patient,on_delete=models.CASCADE)
    date_operation = models.DateTimeField(auto_now_add=True)
    type_operation = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['num_patient','num_medecin','date_operation'],name='patient_medecin_date_operation_unique')
        ]