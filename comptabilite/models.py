from django.db import models

from accueil import models as acmodels

class CarteAssurance(models.Model):
    num_carte_assurance = models.AutoField(primary_key=True)
    num_patient = models.ForeignKey(acmodels.Patient, on_delete=models.CASCADE)
    date_expiration = models.DateField()

    def __str__(self):
        return str(self.num_carte_assurance)

class Paiement(models.Model):
    num_paiement = models.AutoField(primary_key=True)
    num_patient = models.ForeignKey(acmodels.Patient, on_delete=models.CASCADE)
    num_carte_assurance = models.ForeignKey(CarteAssurance, on_delete=models.CASCADE, null=True, blank=True)
    date_paiement = models.DateTimeField(auto_now_add=True)
    montant = models.FloatField()
    objet_paiement = models.CharField(max_length=50)

    def __str__(self):
        return str(self.num_paiement) + " " + str(self.montant) + "gourdes " + self.objet_paiement


class Visite(models.Model):
    num_visite = models.AutoField(primary_key=True)
    num_patient = models.ForeignKey(acmodels.Patient, on_delete=models.CASCADE)
    num_paiement = models.OneToOneField(Paiement, on_delete=models.CASCADE)
    date_visite = models.DateField(auto_now_add=True)
    objectif_visite = models.CharField(max_length=255)



