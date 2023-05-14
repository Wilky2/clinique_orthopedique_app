from django import forms
from . import models
from medecin import models as umodels 

class PaiementForm(forms.ModelForm):
    num_carte_assurance = forms.ModelChoiceField(queryset=models.CarteAssurance.objects.all(),required=False)
    class Meta:
        model = models.Paiement
        fields = ['num_patient', 'num_carte_assurance', 'montant','objet_paiement']

class CarteAssuranceForm(forms.ModelForm):
    date_expiration = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = models.CarteAssurance
        fields = ['num_patient','date_expiration']

class CarteAssuranceModForm(forms.ModelForm):
    date_expiration = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = models.CarteAssurance
        fields = ['date_expiration',]

class ChequeForm(forms.ModelForm):
    date_expiration = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = umodels.Cheque
        fields = ['num_medecin','date_expiration','montant_cheque']
