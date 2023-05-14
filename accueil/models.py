from django.db import models

class Responsable(models.Model):
    num_responsable = models.AutoField(primary_key=True)
    nom_responsable = models.CharField(max_length=20)
    prenom_responsable = models.CharField(max_length=20)
    adresse_responsable = models.CharField(max_length=255)
    no_tel_responsable = models.IntegerField()

    def __str__(self):
        return str(self.num_responsable) + " " + self.nom_responsable + " " + self.prenom_responsable

class Patient (models.Model):
    num_patient = models.AutoField(primary_key=True)
    nom_patient = models.CharField(max_length=20)
    prenom_patient = models.CharField(max_length=20)
    adresse_patient = models.CharField(max_length=255)
    no_tel_patient = models.IntegerField()
    date_naissance = models.DateField()
    groupe_sanguin = models.CharField(max_length=1, null=True,blank=True)

    def __str__(self):
        return str(self.num_patient) + " " + self.nom_patient + " " + self.prenom_patient

class Accompagner(models.Model):
    num_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    num_responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['num_patient','num_responsable'],name='patient_responsable_unique')
        ]


