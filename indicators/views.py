from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.shortcuts import render
from .forms import IndicatorForm, ChangeSportsmenForm, ChartForm, PhysicalIndicatorForm, PsyIndicatorForm, \
    TacticalIndicatorForm, ForSportsmenForm, SportsmenChartForm, UserRegistrationForm, ChangeCategoryForm
from .models import *
from django import forms


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            my_group = Group.objects.get(name='Тренера')
            new_user.groups.add(my_group)

            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def register_sportsmen(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            my_group = Group.objects.get(name='Спортсмены')
            new_user.groups.add(my_group)
            new_user.profile.trainer = request.user
            new_user.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register_sportsmen.html', {'user_form': user_form})


def get_result(name_indicator_model, request, *indicators):
    done_indicators = []
    format_grade = []
    id_user = request.POST.get('user')
    date = str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) + '-' + str(
        request.POST.get('date_day'))
    category = request.POST.get('category')
    for indicator in indicators:
        value = name_indicator_model.objects.filter(date=date, user=id_user).values_list(str(indicator), flat=True)[0]
        obj = Grade.objects.filter(indicator=name_indicator_model._meta.get_field(str(indicator)).verbose_name.title(),
                                   category=category, trainer=request.user)
        if obj:
            if value in range(getattr(obj[0], 'excellent'), getattr(obj[0], 'excellent_border')):
                grade = 5
            elif value in range(getattr(obj[0], 'okay'), getattr(obj[0], 'okay_border') + 1):
                grade = 4
            elif value in range(getattr(obj[0], 'fine'), getattr(obj[0], 'fine_border') + 1):
                grade = 3
            elif value in range(getattr(obj[0], 'satisfactorily'), getattr(obj[0], 'satisfactorily_border')):
                grade = 2
            elif value in range(getattr(obj[0], 'unsatisfactory'), getattr(obj[0], 'unsatisfactory_border')):
                grade = 1
            else:
                grade = 'Выход за указанный диапазон'

        else:
            grade = 'Форматирование оценки не определено'

        done_indicators.append(value)
        format_grade.append(grade)
    return done_indicators, format_grade


def get_result_sportsmen(name_indicator_model, user, request, *indicators):
    done_indicators = []
    format_grade = []
    print(user.profile.trainer)
    date = str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) + '-' + str(
        request.POST.get('date_day'))
    category = request.POST.get('category')
    for indicator in indicators:
        value = name_indicator_model.objects.filter(date=date, user=user).values_list(str(indicator), flat=True)[0]
        obj = Grade.objects.filter(indicator=name_indicator_model._meta.get_field(str(indicator)).verbose_name.title(),
                                   category=category, trainer=user.profile.trainer)
        if obj:
            if value in range(getattr(obj[0], 'excellent'), getattr(obj[0], 'excellent_border')):
                grade = 5
            elif value in range(getattr(obj[0], 'okay'), getattr(obj[0], 'okay_border') + 1):
                grade = 4
            elif value in range(getattr(obj[0], 'fine'), getattr(obj[0], 'fine_border') + 1):
                grade = 3
            elif value in range(getattr(obj[0], 'satisfactorily'), getattr(obj[0], 'satisfactorily_border')):
                grade = 2
            elif value in range(getattr(obj[0], 'unsatisfactory'), getattr(obj[0], 'unsatisfactory_border')):
                grade = 1
            else:
                grade = 'Выход за указанный диапазон'

        else:
            grade = 'Форматирование оценки не определено'

        done_indicators.append(value)
        format_grade.append(grade)
    return done_indicators, format_grade


def get_result_chart(name_indicator_model, request, user, *indicators):
    done_indicators = []
    date_start = str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) + '-' + str(
        request.POST.get('date_day'))
    date_end = str(request.POST.get('end_date_year')) + '-' + str(request.POST.get('end_date_month')) + '-' + str(
        request.POST.get('end_date_day'))
    done_indicators.append(
        name_indicator_model.objects.values('date').filter(user=user, date__range=[date_start, date_end]))
    for indicator in indicators:
        done_indicators.append(
            name_indicator_model.objects.values(indicator).filter(user=user, date__range=[date_start, date_end]))
    return done_indicators


@login_required
def change_user(request):
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        print(request.POST)
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(request.POST)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            request.session['post_request'] = request.POST
            if Indicator.objects.filter(user=request.POST.get('user')) and Indicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.POST.get('user')):
                func_indicators_tuple, grade = get_result(Indicator, request, 'pulse_rate', 'index_of_rufe',
                                                          'coefficient_of_endurance', 'blood_circulation',
                                                          'orthostatic_test', 'clinostatic_test', 'rosenthal_test')
                context = {'form': form, 'pulse_rate': func_indicators_tuple[0],
                           'index_of_rufe': func_indicators_tuple[1],
                           'coefficient_of_endurance': func_indicators_tuple[2],
                           'blood_circulation': func_indicators_tuple[3],
                           'orthostatic_test': func_indicators_tuple[4], 'clinostatic_test': func_indicators_tuple[5],
                           'rosenthal_test': func_indicators_tuple[6], 'grade_pulse_rate': grade[0],
                           'grade_index_of_rufe': grade[1], 'grade_coefficient_of_endurance': grade[2],
                           'grade_blood_circulation': grade[3], 'grade_orthostatic_test': grade[4],
                           'grade_clinostatic_test': grade[5], 'grade_rosenthal_test': grade[6]}

                return render(request, 'table/index.html', context)
        else:
            form = ForSportsmenForm(request.POST)
            request.session['post_request'] = request.POST
            if Indicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.user):
                func_indicators_tuple, grade = get_result_sportsmen(Indicator, request.user, request, 'pulse_rate',
                                                                    'index_of_rufe',
                                                                    'coefficient_of_endurance', 'blood_circulation',
                                                                    'orthostatic_test', 'clinostatic_test',
                                                                    'rosenthal_test')
                context = {'form': form, 'pulse_rate': func_indicators_tuple[0],
                           'index_of_rufe': func_indicators_tuple[1],
                           'coefficient_of_endurance': func_indicators_tuple[2],
                           'blood_circulation': func_indicators_tuple[3],
                           'orthostatic_test': func_indicators_tuple[4], 'clinostatic_test': func_indicators_tuple[5],
                           'rosenthal_test': func_indicators_tuple[6], 'grade_pulse_rate': grade[0],
                           'grade_index_of_rufe': grade[1], 'grade_coefficient_of_endurance': grade[2],
                           'grade_blood_circulation': grade[3], 'grade_orthostatic_test': grade[4],
                           'grade_clinostatic_test': grade[5], 'grade_rosenthal_test': grade[6]}
                return render(request, 'table/index.html', context)
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(post_request)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')

        else:
            form = ForSportsmenForm(post_request)
    return render(request, 'table/index.html', {'form': form,
                                                'pulse_rate': 'Данные не указаны',
                                                'index_of_rufe': 'Данные не указаны',
                                                'coefficient_of_endurance': 'Данные не указаны',
                                                'blood_circulation': 'Данные не указаны',
                                                'orthostatic_test': 'Данные не указаны',
                                                'clinostatic_test': 'Данные не указаны',
                                                'rosenthal_test': 'Данные не указаны'})


@login_required
def physical_indicator(request):
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(request.POST)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            request.session['post_request'] = request.POST
            if PhysicalIndicator.objects.filter(user=request.POST.get('user')) and PhysicalIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.POST.get('user')):
                physical_indicators_tuple, grade = get_result(PhysicalIndicator, request, 'pullups', 'push_ups',
                                                       'sit_up', 'long_jump', 'acceleration', 'six_minute_run',
                                                       'shuttle_run',
                                                       'bridge', 'twine', 'blow_strength', 'flexibility',
                                                       'coordination', 'physical_fitness', 'endurance')
                return render(request, 'table/PhysicalTraining.html',
                              {'form': form, 'pullups': physical_indicators_tuple[0],
                               'push_ups': physical_indicators_tuple[1],
                               'sit_up': physical_indicators_tuple[2],
                               'long_jump': physical_indicators_tuple[3],
                               'acceleration': physical_indicators_tuple[4],
                               'six_minute_run': physical_indicators_tuple[5],
                               'shuttle_run': physical_indicators_tuple[6],
                               'bridge': physical_indicators_tuple[7],
                               'twine': physical_indicators_tuple[8],
                               'blow_strength': physical_indicators_tuple[9],
                               'flexibility': physical_indicators_tuple[10],
                               'coordination': physical_indicators_tuple[11],
                               'physical_fitness': physical_indicators_tuple[12],
                               'endurance': physical_indicators_tuple[13],
                               'grade_pullups': grade[0],
                               'grade_push_ups': grade[1], 'grade_sit_up': grade[2],
                               'grade_long_jump': grade[3], 'grade_acceleration': grade[4],
                               'grade_six_minute_run': grade[5], 'grade_shuttle_run': grade[6],
                               'grade_bridge': grade[7], 'grade_twine': grade[8],
                               'grade_blow_strength': grade[9], 'grade_flexibility': grade[10],
                               'grade_coordination': grade[11], 'grade_physical_fitness': grade[12],
                               'grade_endurance': grade[13]
                               })
        else:
            form = ForSportsmenForm(request.POST)
            request.session['post_request'] = request.POST
            if PhysicalIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.user):
                physical_indicators_tuple = get_result_sportsmen(PhysicalIndicator, request.user, request, 'pullups',
                                                                 'push_ups',
                                                                 'sit_up', 'long_jump', 'acceleration',
                                                                 'six_minute_run',
                                                                 'shuttle_run',
                                                                 'bridge', 'twine', 'blow_strength', 'flexibility',
                                                                 'coordination', 'physical_fitness', 'endurance')
                return render(request, 'table/PhysicalTraining.html',
                              {'form': form, 'pullups': physical_indicators_tuple[0],
                               'push_ups': physical_indicators_tuple[1],
                               'sit_up': physical_indicators_tuple[2],
                               'long_jump': physical_indicators_tuple[3],
                               'acceleration': physical_indicators_tuple[4],
                               'six_minute_run': physical_indicators_tuple[5],
                               'shuttle_run': physical_indicators_tuple[6],
                               'bridge': physical_indicators_tuple[7],
                               'twine': physical_indicators_tuple[8],
                               'blow_strength': physical_indicators_tuple[9],
                               'flexibility': physical_indicators_tuple[10],
                               'coordination': physical_indicators_tuple[11],
                               'physical_fitness': physical_indicators_tuple[12],
                               'endurance': physical_indicators_tuple[13]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(post_request)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form = ForSportsmenForm(post_request)
    return render(request, 'table/PhysicalTraining.html',
                  {'form': form,
                   'pullups': 'Данные не указаны',
                   'push_ups': 'Данные не указаны',
                   'sit_up': 'Данные не указаны',
                   'long_jump': 'Данные не указаны',
                   'acceleration': 'Данные не указаны',
                   'six_minute_run': 'Данные не указаны',
                   'shuttle_run': 'Данные не указаны',
                   'bridge': 'Данные не указаны',
                   'twine': 'Данные не указаны',
                   'blow_strength': 'Данные не указаны',
                   'flexibility': 'Данные не указаны',
                   'coordination': 'Данные не указаны',
                   'physical_fitness': 'Данные не указаны',
                   'endurance': 'Данные не указаны'})


@login_required
def tactical_indicator(request):
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(request.POST)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            request.session['post_request'] = request.POST
            if TacticaIndicator.objects.filter(user=request.POST.get('user')) and TacticaIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.POST.get('user')):
                tactical_indicators_tuple = get_result(TacticaIndicator, request, 'versatility_technical_actions',
                                                       'warfare_ratio',
                                                       'performance_ratio', 'technical_readiness', 'tactical_action',
                                                       'versatility_actions', 'chosen_tactics', 'adjustment_factor',
                                                       'preparatory_actions', 'situational_actions',
                                                       'attack_efficiency',
                                                       'scope_tactical_action', 'protective_actions')
                return render(request, 'table/TacticalTraining.html', {'form': form,
                                                                       'versatility_technical_actions':
                                                                           tactical_indicators_tuple[0],
                                                                       'warfare_ratio': tactical_indicators_tuple[1],
                                                                       'performance_ratio': tactical_indicators_tuple[
                                                                           2],
                                                                       'technical_readiness': tactical_indicators_tuple[
                                                                           3],
                                                                       'tactical_action': tactical_indicators_tuple[4],
                                                                       'versatility_actions': tactical_indicators_tuple[
                                                                           5],
                                                                       'chosen_tactics': tactical_indicators_tuple[6],
                                                                       'adjustment_factor': tactical_indicators_tuple[
                                                                           7],
                                                                       'preparatory_actions': tactical_indicators_tuple[
                                                                           8],
                                                                       'situational_actions': tactical_indicators_tuple[
                                                                           9],
                                                                       'attack_efficiency': tactical_indicators_tuple[
                                                                           10],
                                                                       'scope_tactical_action':
                                                                           tactical_indicators_tuple[
                                                                               11],
                                                                       'protective_actions': tactical_indicators_tuple[
                                                                           12]})
        else:
            form = ForSportsmenForm(request.POST)
            request.session['post_request'] = request.POST
            if TacticaIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.user):
                tactical_indicators_tuple = get_result_sportsmen(TacticaIndicator, request.user, request,
                                                                 'versatility_technical_actions',
                                                                 'warfare_ratio',
                                                                 'performance_ratio', 'technical_readiness',
                                                                 'tactical_action',
                                                                 'versatility_actions', 'chosen_tactics',
                                                                 'adjustment_factor',
                                                                 'preparatory_actions', 'situational_actions',
                                                                 'attack_efficiency',
                                                                 'scope_tactical_action', 'protective_actions')
                return render(request, 'table/TacticalTraining.html', {'form': form,
                                                                       'versatility_technical_actions':
                                                                           tactical_indicators_tuple[0],
                                                                       'warfare_ratio': tactical_indicators_tuple[1],
                                                                       'performance_ratio': tactical_indicators_tuple[
                                                                           2],
                                                                       'technical_readiness': tactical_indicators_tuple[
                                                                           3],
                                                                       'tactical_action': tactical_indicators_tuple[4],
                                                                       'versatility_actions': tactical_indicators_tuple[
                                                                           5],
                                                                       'chosen_tactics': tactical_indicators_tuple[6],
                                                                       'adjustment_factor': tactical_indicators_tuple[
                                                                           7],
                                                                       'preparatory_actions': tactical_indicators_tuple[
                                                                           8],
                                                                       'situational_actions': tactical_indicators_tuple[
                                                                           9],
                                                                       'attack_efficiency': tactical_indicators_tuple[
                                                                           10],
                                                                       'scope_tactical_action':
                                                                           tactical_indicators_tuple[
                                                                               11],
                                                                       'protective_actions': tactical_indicators_tuple[
                                                                           12]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(post_request)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form = ForSportsmenForm(post_request)
    return render(request, 'table/TacticalTraining.html', {'form': form,
                                                           'versatility_technical_actions': 'Данные не указаны',
                                                           'warfare_ratio': 'Данные не указаны',
                                                           'performance_ratio': 'Данные не указаны',
                                                           'technical_readiness': 'Данные не указаны',
                                                           'tactical_action': 'Данные не указаны',
                                                           'versatility_actions': 'Данные не указаны',
                                                           'chosen_tactics': 'Данные не указаны',
                                                           'adjustment_factor': 'Данные не указаны',
                                                           'preparatory_actions': 'Данные не указаны',
                                                           'situational_actions': 'Данные не указаны',
                                                           'attack_efficiency': 'Данные не указаны',
                                                           'scope_tactical_action': 'Данные не указаны',
                                                           'protective_actions': 'Данные не указаны'})


@login_required
def psy_indicator(request):
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(request.POST)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            request.session['post_request'] = request.POST
            if PsyIndicator.objects.filter(user=request.POST.get('user')) and PsyIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.POST.get('user')):
                psy_indicators_tuple = get_result(PsyIndicator, request, 'thermometer_test', 'second_test',
                                                  'persistence_ratio', 'courage_ratio', 'emotional_stability')
                return render(request, 'table/PsychologicalTraining.html',
                              {'form': form, 'thermometer_test': psy_indicators_tuple[0],
                               'second_test': psy_indicators_tuple[1],
                               'persistence_ratio': psy_indicators_tuple[2],
                               'courage_ratio': psy_indicators_tuple[3],
                               'emotional_stability': psy_indicators_tuple[4]})
        else:
            form = ForSportsmenForm(request.POST)
            request.session['post_request'] = request.POST
            if PsyIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.user):
                psy_indicators_tuple = get_result_sportsmen(PsyIndicator, request.user, request, 'thermometer_test',
                                                            'second_test',
                                                            'persistence_ratio', 'courage_ratio', 'emotional_stability')
                return render(request, 'table/PsychologicalTraining.html',
                              {'form': form, 'thermometer_test': psy_indicators_tuple[0],
                               'second_test': psy_indicators_tuple[1],
                               'persistence_ratio': psy_indicators_tuple[2],
                               'courage_ratio': psy_indicators_tuple[3],
                               'emotional_stability': psy_indicators_tuple[4]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(post_request)
            form.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form = ForSportsmenForm(post_request)
    return render(request, 'table/PsychologicalTraining.html', {'form': form, 'thermometer_test': 'Данные не указаны',
                                                                'second_test': 'Данные не указаны',
                                                                'persistence_ratio': 'Данные не указаны',
                                                                'courage_ratio': 'Данные не указаны',
                                                                'emotional_stability': 'Данные не указаны'})


@login_required
@permission_required('indicators.add_indicator')
def grade_formatting(request):
    if request.method == 'POST':

        form_grade_formatting = ChangeCategoryForm(request.POST)
        if form_grade_formatting.is_valid():
            trainer_field = form_grade_formatting.save(commit=False)
            trainer_field.trainer = request.user
            trainer_field.save()
    else:
        form_grade_formatting = ChangeCategoryForm()

    return render(request, 'grade_formatting.html', {'form_grade_formatting': form_grade_formatting})


@login_required
@permission_required('indicators.add_indicator')
def new_indicator(request):
    if request.method == 'POST':
        form_new_indicator = IndicatorForm(request.POST)
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = IndicatorForm()
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
    return render(request, 'add_indicator/new_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
@permission_required('indicators.add_indicator')
def new_physical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PhysicalIndicatorForm(request.POST)
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PhysicalIndicatorForm()
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
    return render(request, 'add_indicator/new_physical_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
@permission_required('indicators.add_indicator')
def new_tactical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = TacticalIndicatorForm(request.POST)
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
        request.session['post_request'] = request.POST
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = TacticalIndicatorForm()
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
    return render(request, 'add_indicator/new_tactical_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
@permission_required('indicators.add_indicator')
def new_psy_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PsyIndicatorForm(request.POST)
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
        request.session['post_request'] = request.POST
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PsyIndicatorForm()
        form_new_indicator.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
            label='Спортсмен')
    return render(request, 'add_indicator/new_psy_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
def charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(request.POST)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            dataset = get_result_chart(Indicator, request, request.POST.get('user'), 'pulse_rate', 'index_of_rufe'
                                       , 'coefficient_of_endurance', 'blood_circulation', 'orthostatic_test',
                                       'clinostatic_test', 'rosenthal_test')
        else:
            form_date = SportsmenChartForm(request.POST)
            dataset = get_result_chart(Indicator, request, request.user, 'pulse_rate', 'index_of_rufe'
                                       , 'coefficient_of_endurance', 'blood_circulation', 'orthostatic_test',
                                       'clinostatic_test', 'rosenthal_test')

        return render(request, 'charts/charts.html', {'formdate': form_date,
                                                      'dataset_date': dataset[0],
                                                      'dataset_pulse_rate': dataset[1],
                                                      'dataset_index_of_rufe': dataset[2],
                                                      'dataset_coefficient_of_endurance': dataset[3],
                                                      'dataset_blood_circulation': dataset[4],
                                                      'dataset_orthostatic_test': dataset[5],
                                                      'dataset_clinostatic_test': dataset[6],
                                                      'dataset_rosenthal_test': dataset[7]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(post_request_chart)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form_date = SportsmenChartForm(post_request_chart)
    return render(request, 'charts/charts.html', {'formdate': form_date})


@login_required
def physical_charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(request.POST)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            dataset = get_result_chart(PhysicalIndicator, request, request.POST.get('user'), 'pullups', 'push_ups',
                                       'long_jump',
                                       'acceleration', 'six_minute_run', 'shuttle_run',
                                       'bridge', 'twine', 'blow_strength', 'endurance', 'flexibility',
                                       'coordination', 'physical_fitness', 'sit_up')
        else:
            form_date = SportsmenChartForm(request.POST)
            dataset = get_result_chart(PhysicalIndicator, request, request.user, 'pullups', 'push_ups', 'long_jump',
                                       'acceleration', 'six_minute_run', 'shuttle_run',
                                       'bridge', 'twine', 'blow_strength', 'endurance', 'flexibility',
                                       'coordination', 'physical_fitness', 'sit_up')

        return render(request, 'charts/physical_charts.html', {'formdate': form_date,
                                                               'dataset_date': dataset[0],
                                                               'dataset_pullups': dataset[1],
                                                               'dataset_push_ups': dataset[2],
                                                               'dataset_long_jump': dataset[3],
                                                               'dataset_acceleration': dataset[4],
                                                               'dataset_six_minute_run': dataset[5],
                                                               'dataset_shuttle_run': dataset[6],
                                                               'dataset_bridge': dataset[7],
                                                               'dataset_twine': dataset[8],
                                                               'dataset_blow_strength': dataset[9],
                                                               'dataset_endurance': dataset[10],
                                                               'dataset_flexibility': dataset[11],
                                                               'dataset_coordination': dataset[12],
                                                               'dataset_physical_fitness': dataset[13],
                                                               'dataset_sit_up': dataset[14]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(post_request_chart)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form_date = SportsmenChartForm(post_request_chart)
    return render(request, 'charts/physical_charts.html', {'formdate': form_date})


@login_required
def tactical_charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(request.POST)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            dataset = get_result_chart(TacticaIndicator, request, request.POST.get('user'),
                                       'versatility_technical_actions',
                                       'attack_efficiency', 'warfare_ratio',
                                       'performance_ratio', 'technical_readiness', 'tactical_action',
                                       'versatility_actions', 'chosen_tactics', 'adjustment_factor',
                                       'preparatory_actions', 'situational_actions',
                                       'scope_tactical_action', 'protective_actions')
        else:
            form_date = SportsmenChartForm(request.POST)
            dataset = get_result_chart(TacticaIndicator, request, request.user, 'versatility_technical_actions',
                                       'attack_efficiency', 'warfare_ratio',
                                       'performance_ratio', 'technical_readiness', 'tactical_action',
                                       'versatility_actions', 'chosen_tactics', 'adjustment_factor',
                                       'preparatory_actions', 'situational_actions',
                                       'scope_tactical_action', 'protective_actions')

        return render(request, 'charts/tactical_charts.html', {'formdate': form_date,
                                                               'dataset_date': dataset[0],
                                                               'dataset_versatility_technical_actions': dataset[1],
                                                               'dataset_attack_efficiency': dataset[2],
                                                               'dataset_warfare_ratio': dataset[3],
                                                               'dataset_performance_ratio': dataset[4],
                                                               'dataset_technical_readiness': dataset[5],
                                                               'dataset_tactical_action': dataset[6],
                                                               'dataset_versatility_actions': dataset[7],
                                                               'dataset_chosen_tactics': dataset[8],
                                                               'dataset_adjustment_factor': dataset[9],
                                                               'dataset_preparatory_actions': dataset[10],
                                                               'dataset_situational_actions': dataset[11],
                                                               'dataset_scope_tactical_action': dataset[12],
                                                               'dataset_protective_actions': dataset[13]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(post_request_chart)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form_date = SportsmenChartForm(post_request_chart)
    return render(request, 'charts/tactical_charts.html', {'formdate': form_date})


@login_required
def psy_charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(request.POST)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
            dataset = get_result_chart(PsyIndicator, request, request.POST.get('user'), 'thermometer_test',
                                       'second_test',
                                       'persistence_ratio', 'courage_ratio', 'emotional_stability')
        else:
            form_date = SportsmenChartForm(request.POST)
            dataset = get_result_chart(PsyIndicator, request, request.user, 'thermometer_test', 'second_test',
                                       'persistence_ratio', 'courage_ratio', 'emotional_stability')

        return render(request, 'charts/psy_charts.html', {'formdate': form_date,
                                                          'dataset_date': dataset[0],
                                                          'dataset_thermometer_test': dataset[1],
                                                          'dataset_second_test': dataset[2],
                                                          'dataset_persistence_ratio': dataset[3],
                                                          'dataset_courage_ratio': dataset[4],
                                                          'dataset_emotional_stability': dataset[5]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(post_request_chart)
            form_date.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(profile__trainer=request.user).select_related('profile'),
                label='Спортсмен')
        else:
            form_date = SportsmenChartForm(post_request_chart)
    return render(request, 'charts/psy_charts.html', {'formdate': form_date})
