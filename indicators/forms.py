from .models import *
from django import forms


class ChangeSportsmenForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ('user', 'date')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ('user','date','pulse_rate','index_of_rufe','coefficient_of_endurance')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class PhysicalIndicatorForm(forms.ModelForm):
    class Meta:
        model = PhysicalIndicator
        fields = ('user','date','pullups','push_ups','sit_up')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class TacticalIndicatorForm(forms.ModelForm):
    class Meta:
        model = TacticaIndicator
        fields = ('user','date','versatility_technical_actions','attack_efficiency','protective_actions')
        widgets = {
            'date': forms.SelectDateWidget()
        }


class PsyIndicatorForm(forms.ModelForm):
    class Meta:
        model = PsyIndicator
        fields = ('user','date','thermometer_test','second_test','emotional_stability')
        widgets = {
            'date': forms.SelectDateWidget()
        }

class ChartForm(forms.ModelForm):
    end_date = forms.DateField(widget = forms.SelectDateWidget, label='Конечная дата')

    class Meta:
        model = Indicator
        fields = ('user', 'date')
        widgets = {
            'date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget()
        }
        labels = {
            'date': ('Начальная дата'),
        }
