from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.shortcuts import render
from .forms import IndicatorForm, ChangeSportsmenForm, ChartForm, PhysicalIndicatorForm, PsyIndicatorForm, \
    TacticalIndicatorForm, ForSportsmenForm, SportsmenChartForm, UserRegistrationForm
from .models import *


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            my_group = Group.objects.get(name='Тренера')
            new_user.groups.add(my_group)

            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def get_result(name_indicator_model, request, *indicators):
    done_indicators = []
    id_user = request.POST.get('user')
    date = str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) + '-' + str(
        request.POST.get('date_day'))
    for indicator in indicators:
        done_indicators.append(
            name_indicator_model.objects.filter(date=date, user=id_user).values_list(str(indicator), flat=True)[0])
    return done_indicators


def get_result_sportsmen(name_indicator_model, user, request, *indicators):
    done_indicators = []
    date = str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) + '-' + str(
        request.POST.get('date_day'))
    for indicator in indicators:
        done_indicators.append(
            name_indicator_model.objects.filter(date=date, user=user).values_list(str(indicator), flat=True)[0])
    return done_indicators


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
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(request.POST)
            request.session['post_request'] = request.POST
            if Indicator.objects.filter(user=request.POST.get('user')) and Indicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.POST.get('user')):
                func_indicators_tuple = get_result(Indicator, request, 'pulse_rate', 'index_of_rufe',
                                                   'coefficient_of_endurance', 'blood_circulation',
                                                   'orthostatic_test', 'clinostatic_test', 'rosenthal_test')
                return render(request, 'table/index.html', {'form': form,
                                                            'pulse_rate': func_indicators_tuple[0],
                                                            'index_of_rufe': func_indicators_tuple[1],
                                                            'coefficient_of_endurance': func_indicators_tuple[2],
                                                            'blood_circulation': func_indicators_tuple[3],
                                                            'orthostatic_test': func_indicators_tuple[4],
                                                            'clinostatic_test': func_indicators_tuple[5],
                                                            'rosenthal_test': func_indicators_tuple[6]})
        else:
            form = ForSportsmenForm(request.POST)
            request.session['post_request'] = request.POST
            if Indicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.user):
                func_indicators_tuple = get_result_sportsmen(Indicator, request.user, request, 'pulse_rate',
                                                             'index_of_rufe',
                                                             'coefficient_of_endurance', 'blood_circulation',
                                                             'orthostatic_test', 'clinostatic_test', 'rosenthal_test')
                return render(request, 'table/index.html', {'form': form,
                                                            'pulse_rate': func_indicators_tuple[0],
                                                            'index_of_rufe': func_indicators_tuple[1],
                                                            'coefficient_of_endurance': func_indicators_tuple[2],
                                                            'blood_circulation': func_indicators_tuple[3],
                                                            'orthostatic_test': func_indicators_tuple[4],
                                                            'clinostatic_test': func_indicators_tuple[5],
                                                            'rosenthal_test': func_indicators_tuple[6]})
    else:
        if request.user.has_perm('indicators.add_indicator'):
            form = ChangeSportsmenForm(post_request)
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
            request.session['post_request'] = request.POST
            if PhysicalIndicator.objects.filter(user=request.POST.get('user')) and PhysicalIndicator.objects.filter(
                    date=str(request.POST.get('date_year')) + '-' + str(request.POST.get('date_month')) +
                         '-' + str(request.POST.get('date_day')), user=request.POST.get('user')):
                physical_indicators_tuple = get_result(PhysicalIndicator, request, 'pullups', 'push_ups',
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
                               'endurance': physical_indicators_tuple[13]})
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
        else:
            form = ForSportsmenForm(post_request)
    return render(request, 'table/PsychologicalTraining.html', {'form': form, 'thermometer_test': 'Данные не указаны',
                                                                'second_test': 'Данные не указаны',
                                                                'persistence_ratio': 'Данные не указаны',
                                                                'courage_ratio': 'Данные не указаны',
                                                                'emotional_stability': 'Данные не указаны'})


@login_required
@permission_required('indicators.add_indicator')
def new_indicator(request):
    if request.method == 'POST':
        form_new_indicator = IndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = IndicatorForm()
    return render(request, 'add_indicator/new_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
@permission_required('indicators.add_indicator')
def new_physical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PhysicalIndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PhysicalIndicatorForm()
    return render(request, 'add_indicator/new_physical_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
@permission_required('indicators.add_indicator')
def new_tactical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = TacticalIndicatorForm(request.POST)
        request.session['post_request'] = request.POST
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = TacticalIndicatorForm()
    return render(request, 'add_indicator/new_tactical_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
@permission_required('indicators.add_indicator')
def new_psy_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PsyIndicatorForm(request.POST)
        request.session['post_request'] = request.POST
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PsyIndicatorForm()
    return render(request, 'add_indicator/new_psy_indicator.html', {'form_new_indicator': form_new_indicator})


@login_required
def charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        if request.user.has_perm('indicators.add_indicator'):
            form_date = ChartForm(request.POST)
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
            dataset = get_result_chart(PsyIndicator, request, request.POST.get('user'), 'thermometer_test', 'second_test',
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
        else:
            form_date = SportsmenChartForm(post_request_chart)
    return render(request, 'charts/psy_charts.html', {'formdate': form_date})