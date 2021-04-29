from django.contrib import admin
from .models import Indicator

class IndicatoAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('user', 'date')

admin.site.register(Indicator, IndicatoAdmin)
