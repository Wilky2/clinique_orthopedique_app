from django.contrib import admin

from . import models 

class CarteAssuranceAdmin(admin.ModelAdmin):
    list_display = ('num_carte_assurance','num_patient','date_expiration')

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('num_paiement','objet_paiement','montant')

admin.site.register(models.Paiement, PaiementAdmin)
admin.site.register(models.CarteAssurance, CarteAssuranceAdmin)