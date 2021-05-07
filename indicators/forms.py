

from .models import *
from django import forms
from datetime import date



class ChangeSportsmenForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ('user', 'date')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class ForSportsmenForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ('date',)
        widgets = {
            'date': forms.SelectDateWidget()
        }


class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ('__all__')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class PhysicalIndicatorForm(forms.ModelForm):
    class Meta:
        model = PhysicalIndicator
        fields = ('__all__')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class TacticalIndicatorForm(forms.ModelForm):
    class Meta:
        model = TacticaIndicator
        fields = ('__all__')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class PsyIndicatorForm(forms.ModelForm):
    class Meta:
        model = PsyIndicator
        fields = ('__all__')
        widgets = {
            'date': forms.SelectDateWidget()
        }

class ChartForm(forms.ModelForm):
    end_date = forms.DateField(widget = forms.SelectDateWidget, label='Конечная дата', initial=date.today)

    class Meta:
        model = Indicator
        fields = ('user', 'date')
        widgets = {
            'date': forms.SelectDateWidget()
        }
        labels = {
            'date': ('Начальная дата'),
        }
