from django import forms

from . import models

class OperationForm(forms.ModelForm):

    class Meta:
        model = models.Operer
        fields = ['num_medecin','num_patient','type_operation']