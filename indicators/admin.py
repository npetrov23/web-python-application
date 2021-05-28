from datetime import datetime

from django.contrib import admin
from import_export import resources
from .models import *
from import_export.admin import ImportExportModelAdmin




class IndicatoAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('user', 'date')


class PhysicalIndicatorExportImport(resources.ModelResource):

    class Meta:
        model = PhysicalIndicator
        widgets = {
                'date': {'format': '%d/%m/%y'},
                }


class PhysicalIndicatorAdm(ImportExportModelAdmin):
    resource_class = PhysicalIndicatorExportImport
    list_display = ('user', 'date')
    list_filter = ('user', 'date')

admin.site.register(Indicator, PhysicalIndicatorAdm)
admin.site.register(PhysicalIndicator, PhysicalIndicatorAdm)
admin.site.register(TacticaIndicator, PhysicalIndicatorAdm)
admin.site.register(PsyIndicator, PhysicalIndicatorAdm)
admin.site.register(Grade)

#admin.site.register(Profile)
