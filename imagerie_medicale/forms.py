from django import forms

from . import models

class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = models.Prescription
        fields = '__all__'

class RendezVousForm(forms.ModelForm):
    date_rendez_vous = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = models.RendezVous
        fields = '__all__'

class ExamenForm(forms.ModelForm):

    class Meta:
        model = models.Examiner
        fields = ['num_medecin','num_patient','type_examen','diagnostic_examen']