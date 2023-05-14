from django.db import models
from authentication.models import User

class Poste(models.Model):
    nom_poste = models.CharField(max_length=20,primary_key=True)
    salaire = models.FloatField()

    def __str__(self):
        return self.nom_poste

class Medecin(models.Model):
    num_medecin = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    nom_poste = models.ForeignKey(Poste, on_delete=models.CASCADE,null=True,blank=True)
    num_medecin_chef = models.IntegerField()
    nom_medecin = models.CharField(max_length=20)
    prenom_medecin = models.CharField(max_length=20)

    def __str__(self):
        return str(self.num_medecin) + " " + str(self.nom_medecin) + " " + str(self.prenom_medecin)

class Horaire(models.Model):
    num_horaire = models.AutoField(primary_key=True)
    jour_horaire = models.CharField(max_length=10)
    heure_horaire = models.TimeField()

class Attribuer(models.Model):
    num_medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    num_horaire = models.ForeignKey(Horaire, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['num_horaire','num_medecin'],name='horaire_medecin_unique')
        ]

class Cheque(models.Model):
    num_cheque = models.AutoField(primary_key=True)
    num_medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_emission = models.DateField(auto_now_add=True)
    date_expiration = models.DateField()
    montant_cheque = models.FloatField()


class Specialiser(models.Model):
    specialite = models.CharField(max_length=50)
    domaine = models.CharField(max_length=50)
    num_medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    type_intervention = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(fields=['specialite','num_medecin','domaine'],name='specialite_medecin_domaine_unique')
        ]



