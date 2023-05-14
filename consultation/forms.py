from django import forms

from . import models

class DossierForm(forms.ModelForm):

    class Meta:
        model = models.Dossier
        fields = ['num_patient',]

class ConsultationForm(forms.ModelForm):

    class Meta:
        model = models.Consulter
        fields = ['num_medecin','num_patient','tension_corporelle','resultat_consultation']
