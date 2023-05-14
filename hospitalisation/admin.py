from django.contrib import admin

from . import models

class HospitaliserAdmin(admin.ModelAdmin):
    list_display = ['num_medecin','num_patient','date_debut_hospitalisation']



admin.site.register(models.Hospitaliser, HospitaliserAdmin)
