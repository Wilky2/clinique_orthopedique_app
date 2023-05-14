from django.contrib import admin

from . import models

class DossierAdmin(admin.ModelAdmin):
    list_display = ['num_dossier','num_patient','etat_dossier']

class ConsulterAdmin(admin.ModelAdmin):
    list_display = ['num_medecin','num_patient','date_consultation']


admin.site.register(models.Dossier, DossierAdmin)
admin.site.register(models.Consulter, ConsulterAdmin)