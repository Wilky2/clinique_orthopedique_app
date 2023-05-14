from django.contrib import admin

from . import models

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['num_prescription','num_medecin','num_patient']

class RendezVousAdmin(admin.ModelAdmin):
    list_display = ['num_rendez_vous','num_medecin','num_patient']


class ExaminerAdmin(admin.ModelAdmin):
    list_display = ['num_medecin','num_patient','date_examen']



admin.site.register(models.Prescription, PrescriptionAdmin)
admin.site.register(models.RendezVous, RendezVousAdmin)
admin.site.register(models.Examiner, ExaminerAdmin)
