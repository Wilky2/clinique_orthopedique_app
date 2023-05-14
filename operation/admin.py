from django.contrib import admin

from . import models


class OpererAdmin(admin.ModelAdmin):
    list_display = ['num_medecin','num_patient','date_operation']

admin.site.register(models.Operer, OpererAdmin)
