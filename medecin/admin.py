from django.contrib import admin

from . import models


class PosteAdmin(admin.ModelAdmin):
    list_display = ['nom_poste','salaire']

class MedecinAdmin(admin.ModelAdmin):
    list_display = ['num_medecin','nom_medecin','prenom_medecin']

class HoraireAdmin(admin.ModelAdmin):
    list_display = ['num_horaire','jour_horaire','heure_horaire']

class AttribuerAdmin(admin.ModelAdmin):
    list_display = ['num_horaire','num_medecin']

class ChequeAdmin(admin.ModelAdmin):
    list_display = ['num_cheque','num_medecin','montant_cheque']

class SpecialiserAdmin(admin.ModelAdmin):
    list_display = ['num_medecin','domaine', 'specialite']

admin.site.register(models.Poste, PosteAdmin)
admin.site.register(models.Medecin, MedecinAdmin)
admin.site.register(models.Horaire, HoraireAdmin)
admin.site.register(models.Attribuer, AttribuerAdmin)
admin.site.register(models.Cheque, ChequeAdmin)
admin.site.register(models.Specialiser, SpecialiserAdmin)