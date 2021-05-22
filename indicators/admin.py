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
                'date': {'format': '%d.%m.%Y'},
                }


class PhysicalIndicatorAdm(ImportExportModelAdmin):
    resource_class = PhysicalIndicatorExportImport


admin.site.register(Indicator, IndicatoAdmin)
admin.site.register(PhysicalIndicator, PhysicalIndicatorAdm)
admin.site.register(TacticaIndicator, IndicatoAdmin)
admin.site.register(PsyIndicator, IndicatoAdmin)
admin.site.register(Profile)
