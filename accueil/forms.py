from django import forms
from . import models
from comptabilite.models import Visite 

class PatientForm(forms.ModelForm):
    date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Patient
        fields = '__all__'

class ResponsableForm(forms.ModelForm):

    class Meta:
        model = models.Responsable
        fields = '__all__'

class AccompagnerForm(forms.ModelForm):

    class Meta:
        model = models.Accompagner
        fields = ['num_responsable']

class VisiteForm(forms.ModelForm):

    class Meta:
        model = Visite
        fields = ['num_patient', 'num_paiement', 'objectif_visite']