

from .models import *
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': ('Логин для входа'),
            'first_name': ('Имя спортсмена'),
            'last_name': ('Фамилия спортсмена'),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ChangeSportsmenForm(forms.ModelForm):
    #user = forms.ModelChoiceField(queryset=Profile.objects.all())

    class Meta:
        model = Indicator
        fields = ('user', 'date')
        widgets = {
            'date': forms.SelectDateWidget(),
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


class SportsmenChartForm(forms.ModelForm):
    end_date = forms.DateField(widget = forms.SelectDateWidget, label='Конечная дата', initial=date.today)

    class Meta:
        model = Indicator
        fields = ('date',)
        widgets = {
            'date': forms.SelectDateWidget()
        }
        labels = {
            'date': ('Начальная дата'),
        }