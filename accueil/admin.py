from django.contrib import admin

from . import models
from comptabilite.models import Visite

class PatientAdmin(admin.ModelAdmin):
    list_display = ('num_patient','nom_patient','prenom_patient')

class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('num_responsable','nom_responsable','prenom_responsable')

class AccompagnerAdmin(admin.ModelAdmin):
    list_display = ('num_patient','num_responsable')

class VisiteAdmin(admin.ModelAdmin):
    list_display = ('num_visite','num_patient','objectif_visite')

admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Responsable, ResponsableAdmin)
admin.site.register(models.Accompagner, AccompagnerAdmin)
admin.site.register(Visite, VisiteAdmin)
