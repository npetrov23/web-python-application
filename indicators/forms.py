from .models import *
from django import forms
from datetime import date
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    captcha = ReCaptchaField(label='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

INDICATORS_NAME = (
    ("Чпп", "Чпп"),
    ("Проба Руффье", "Проба Руффье"),
    ("Коэффициент Выносливости", "Коэффициент Выносливости"),
    ("Коэффициент Экономичности Кровообращения", "Коэффициент Экономичности Кровообращения"),
    ("Ортостатическая Проба", "Ортостатическая Проба"),
    ("Клиностатическая Проба", "Клиностатическая Проба"),
    ("Проба Розенталя", "Проба Розенталя"),
    ("Подтягивания", "Подтягивания"),
    ("Отжимания", "Отжимания"),
    ('Пресс "Складка"', 'Пресс "Складка"'),
    ("Прыжок В Длину С Места", "Прыжок В Длину С Места"),
    ("Ускорение 100М (C)", "Ускорение 100М (C)"),
    ("6-Ти Минутный Бег (М)", "6-Ти Минутный Бег (М)"),
    ('"Мостик" (См)', '"Мостик" (См)'),
    ('"Шпагат" (См)', '"Шпагат" (См)'),
    ("Сила Ударов (%)", "Сила Ударов (%)"),
    ("Гибкость (%)", "Гибкость (%)"),
    ("Ккс (%)", "Ккс (%)"),
    ("Ксфп (%)", "Ксфп (%)"),
    ("Выносливость (%)", "Выносливость (%)"),
    ("Коэффициент Объема Технических Действий", "Коэффициент Объема Технических Действий"),
    ("Коэффициент Результативности", "Коэффициент Результативности"),
    ("Техническая Подготовленность", "Техническая Подготовленность"),
    ("Тактическая Подготовленность", "Тактическая Подготовленность"),
    ("Разносторонность Тактических Действий", "Разносторонность Тактических Действий"),
    ("Коэффициент Избранной Тактики", "Коэффициент Избранной Тактики"),
    ("Коэффициент Перестройки Тактики", "Коэффициент Перестройки Тактики"),
    ("Коэффициент Подготовительных Тактических Действий", "Коэффициент Подготовительных Тактических Действий"),
    ("Коэффициент Ситуативных Тактических Действий", "Коэффициент Ситуативных Тактических Действий"),
    ("Коэффициент Эффективности Атакующих Действий", "Коэффициент Эффективности Атакующих Действий"),
    ("Коэффициент Объема Тактических Действий", "Коэффициент Объема Тактических Действий"),
    ("Коэффициент Эффективности Защитных Действий", "Коэффициент Эффективности Защитных Действий"),
    ('Тест "Градусник"', 'Тест "Градусник"'),
    ('Тест "10 Секунд"', 'Тест "10 Секунд"'),
    ("Коэффициент Настойчивости", "Коэффициент Настойчивости"),
    ("Коэффициент Смелости", "Коэффициент Смелости"),
    ("Коэффициент Эмоциональной Устойчивости", "Коэффициент Эмоциональной Устойчивости"),
)

CATEGORY = (
    ("Юноши и девушки", "Юноши и девушки"),
    ("Юниоры и юниорки", "Юниоры и юниорки"),
    ("Взрослые", "Взрослые"),
)

class ChangeCategoryForm(forms.ModelForm):
    indicator = forms.ChoiceField(choices=INDICATORS_NAME, label='Статистический показатель')
    category = forms.ChoiceField(choices=CATEGORY, label='Категория')
    class Meta:
        model = Grade
        exclude = ('trainer',)

class ChangeSportsmenForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY, label='Категория')

    class Meta:
        model = Indicator
        fields = ('user', 'date')
        widgets = {
            'date': forms.SelectDateWidget(),
        }



class ForSportsmenForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY, label='Категория')

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