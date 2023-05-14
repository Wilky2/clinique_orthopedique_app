from django import forms

from . import models

class HospitalisationForm(forms.ModelForm):
    date_fin_hospitalisation = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}),required=False)
    class Meta:
        model = models.Hospitaliser
        fields = ['num_medecin','num_patient','date_fin_hospitalisation']

class HospitalisationModForm(forms.ModelForm):
    date_fin_hospitalisation = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}),required=False)
    class Meta:
        model = models.Hospitaliser
        fields = ['date_fin_hospitalisation',]
