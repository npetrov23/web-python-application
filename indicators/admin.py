from django.contrib import admin
from .models import *


class IndicatoAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('user', 'date')

admin.site.register(Indicator, IndicatoAdmin)
admin.site.register(PhysicalIndicator, IndicatoAdmin)
admin.site.register(TacticaIndicator, IndicatoAdmin)
admin.site.register(PsyIndicator, IndicatoAdmin)
