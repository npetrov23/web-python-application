from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import IndicatorForm, ChangeSportsmenForm, ChartForm, PhysicalIndicatorForm, PsyIndicatorForm, \
    TacticalIndicatorForm
from .models import *


@login_required
def change_user(request):
    pulse_rate = 0
    index_of_rufe = 0
    coefficient_of_endurance = 0
    blood_circulation = 0
    orthostatic_test = 0
    clinostatic_test = 0
    rosenthal_test = 0
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        request.session['post_request'] = request.POST
        if Indicator.objects.filter(user=request.POST.get('user')) and \
                Indicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            pulse_rate = Indicator.objects.filter(date=date,user=id_user).values_list('pulse_rate', flat=True)[0]
            index_of_rufe = Indicator.objects.filter(date=date,user=id_user).values_list('index_of_rufe', flat=True)[0]
            coefficient_of_endurance = Indicator.objects.filter(date=date,user=id_user).values_list('coefficient_of_endurance', flat=True)[0]
            blood_circulation = Indicator.objects.filter(date=date,user=id_user).values_list('blood_circulation', flat=True)[0]
            orthostatic_test = Indicator.objects.filter(date=date,user=id_user).values_list('orthostatic_test', flat=True)[0]
            clinostatic_test = Indicator.objects.filter(date=date,user=id_user).values_list('clinostatic_test', flat=True)[0]
            rosenthal_test = Indicator.objects.filter(date=date,user=id_user).values_list('rosenthal_test', flat=True)[0]
    else:
        form = ChangeSportsmenForm(post_request)
    return render(request, 'table/index.html', {'form':form, 'pulse_rate': pulse_rate, 'index_of_rufe': index_of_rufe, 'coefficient_of_endurance': coefficient_of_endurance,
                                        'blood_circulation':blood_circulation,
                                        'orthostatic_test':orthostatic_test,
                                        'clinostatic_test':clinostatic_test,
                                        'rosenthal_test':rosenthal_test})

@login_required
def physical_indicator(request):
    pullups = 0
    push_ups = 0
    sit_up = 0
    long_jump = 0
    acceleration = 0
    six_minute_run = 0
    shuttle_run = 0
    bridge = 0
    twine = 0
    blow_strength = 0
    endurance = 0
    flexibility = 0
    coordination = 0
    physical_fitness = 0
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        request.session['post_request'] = request.POST
        if PhysicalIndicator.objects.filter(user=request.POST.get('user')) and \
                PhysicalIndicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            pullups = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('pullups', flat=True)[0]
            push_ups = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('push_ups', flat=True)[0]
            sit_up = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('sit_up', flat=True)[0]
            long_jump = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('long_jump', flat=True)[0]
            acceleration = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('acceleration', flat=True)[0]
            six_minute_run = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('six_minute_run', flat=True)[0]
            shuttle_run = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('shuttle_run', flat=True)[0]
            bridge = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('bridge', flat=True)[0]
            twine = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('twine', flat=True)[0]
            blow_strength = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('blow_strength', flat=True)[0]
            endurance = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('endurance', flat=True)[0]
            flexibility = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('flexibility', flat=True)[0]
            coordination = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('coordination', flat=True)[0]
            physical_fitness = PhysicalIndicator.objects.filter(date=date,user=id_user).values_list('physical_fitness', flat=True)[0]
    else:
        form = ChangeSportsmenForm(post_request)

    return render(request, 'table/PhysicalTraining.html', {'form':form, 'pullups': pullups, 'push_ups': push_ups, 'sit_up': sit_up,
                                                   'long_jump':long_jump,
                                                    'acceleration':acceleration,
                                                    'six_minute_run':six_minute_run,
                                                    'shuttle_run':shuttle_run,
                                                    'bridge':bridge,
                                                    'twine':twine,
                                                    'blow_strength':blow_strength,
                                                    'flexibility': flexibility,
                                                    'coordination': coordination,
                                                    'physical_fitness': physical_fitness,
                                                           'endurance': endurance})

@login_required
def tactical_indicator(request):
    versatility_technical_actions = 0
    attack_efficiency = 0
    protective_actions = 0
    warfare_ratio = 0
    performance_ratio = 0
    technical_readiness = 0
    tactical_action = 0
    versatility_actions = 0
    chosen_tactics = 0
    adjustment_factor = 0
    preparatory_actions = 0
    situational_actions = 0
    scope_tactical_action = 0
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        request.session['post_request'] = request.POST
        if TacticaIndicator.objects.filter(user=request.POST.get('user')) and \
                TacticaIndicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            versatility_technical_actions = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('versatility_technical_actions', flat=True)[0]
            attack_efficiency = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('attack_efficiency', flat=True)[0]
            protective_actions = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('protective_actions', flat=True)[0]
            warfare_ratio = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('warfare_ratio', flat=True)[0]
            performance_ratio = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('performance_ratio', flat=True)[0]
            technical_readiness = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('technical_readiness', flat=True)[0]
            tactical_action = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('tactical_action', flat=True)[0]
            versatility_actions = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('versatility_actions', flat=True)[0]
            chosen_tactics = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('chosen_tactics', flat=True)[0]
            adjustment_factor = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('adjustment_factor', flat=True)[0]
            preparatory_actions = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('preparatory_actions', flat=True)[0]
            situational_actions = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('situational_actions', flat=True)[0]
            scope_tactical_action = TacticaIndicator.objects.filter(date=date,user=id_user).values_list('scope_tactical_action', flat=True)[0]

    else:
        form = ChangeSportsmenForm(post_request)
    return render(request, 'table/TacticalTraining.html', {'form':form,
                                                   'versatility_technical_actions': versatility_technical_actions,
                                                   'warfare_ratio': warfare_ratio,
                                                   'performance_ratio': performance_ratio,
                                                   'technical_readiness': technical_readiness,
                                                   'tactical_action': tactical_action,
                                                   'versatility_actions': versatility_actions,
                                                   'chosen_tactics': chosen_tactics,
                                                   'adjustment_factor': adjustment_factor,
                                                   'preparatory_actions': preparatory_actions,
                                                   'situational_actions': situational_actions,
                                                           'attack_efficiency': attack_efficiency,
                                                           'scope_tactical_action': scope_tactical_action,
                                                           'protective_actions': protective_actions})

@login_required
def psy_indicator(request):
    thermometer_test = 0
    second_test = 0
    emotional_stability = 0
    persistence_ratio = 0
    courage_ratio = 0
    post_request = request.session.get('post_request', None)
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        request.session['post_request'] = request.POST
        #if form.is_valid():
        if PsyIndicator.objects.filter(user=request.POST.get('user')) and \
                PsyIndicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            thermometer_test = PsyIndicator.objects.filter(date=date,user=id_user).values_list('thermometer_test', flat=True)[0]
            second_test = PsyIndicator.objects.filter(date=date,user=id_user).values_list('second_test', flat=True)[0]
            emotional_stability = PsyIndicator.objects.filter(date=date,user=id_user).values_list('emotional_stability', flat=True)[0]
            persistence_ratio = PsyIndicator.objects.filter(date=date,user=id_user).values_list('persistence_ratio', flat=True)[0]
            courage_ratio = PsyIndicator.objects.filter(date=date,user=id_user).values_list('courage_ratio', flat=True)[0]
    else:
        form = ChangeSportsmenForm(post_request)
    return render(request, 'table/PsychologicalTraining.html', {'form':form, 'thermometer_test': thermometer_test,
                                                        'second_test': second_test,
                                                        'persistence_ratio': persistence_ratio,
                                                        'courage_ratio': courage_ratio,
                                                        'emotional_stability': emotional_stability})


@login_required
def new_indicator(request):
    if request.method == 'POST':
        form_new_indicator = IndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = IndicatorForm()
    return render(request, 'add_indicator/new_indicator.html', {'form_new_indicator':form_new_indicator})

@login_required
def new_physical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PhysicalIndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PhysicalIndicatorForm()
    return render(request, 'add_indicator/new_physical_indicator.html', {'form_new_indicator':form_new_indicator})

@login_required
def new_tactical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = TacticalIndicatorForm(request.POST)
        request.session['post_request'] = request.POST
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = TacticalIndicatorForm()
    return render(request, 'add_indicator/new_tactical_indicator.html', {'form_new_indicator':form_new_indicator})

@login_required
def new_psy_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PsyIndicatorForm(request.POST)
        request.session['post_request'] = request.POST
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PsyIndicatorForm()
    return render(request, 'add_indicator/new_psy_indicator.html', {'form_new_indicator':form_new_indicator})

@login_required
def charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = Indicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_pulse_rate = Indicator.objects.values('pulse_rate').filter(user=id_user, date__range=[date_start, date_end])
        dataset_index_of_rufe = Indicator.objects.values('index_of_rufe').filter(user=id_user, date__range=[date_start, date_end])
        dataset_coefficient_of_endurance = Indicator.objects.values('coefficient_of_endurance').filter(user=id_user, date__range=[date_start, date_end])
        dataset_blood_circulation = Indicator.objects.values('blood_circulation').filter(user=id_user, date__range=[date_start, date_end])
        dataset_orthostatic_test = Indicator.objects.values('orthostatic_test').filter(user=id_user, date__range=[date_start, date_end])
        dataset_clinostatic_test = Indicator.objects.values('clinostatic_test').filter(user=id_user, date__range=[date_start, date_end])
        dataset_rosenthal_test = Indicator.objects.values('rosenthal_test').filter(user=id_user, date__range=[date_start, date_end])
    else:
        formdate = ChartForm(post_request_chart)
        dataset_date = ['']
        dataset_pulse_rate = []
        dataset_index_of_rufe = []
        dataset_coefficient_of_endurance = []
        dataset_blood_circulation = []
        dataset_orthostatic_test = []
        dataset_clinostatic_test = []
        dataset_rosenthal_test = []
    return render(request, 'charts/charts.html', {'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_pulse_rate':dataset_pulse_rate,
                                          'dataset_index_of_rufe':dataset_index_of_rufe,
                                          'dataset_blood_circulation': dataset_blood_circulation,
                                          'dataset_orthostatic_test': dataset_orthostatic_test,
                                          'dataset_clinostatic_test': dataset_clinostatic_test,
                                          'dataset_rosenthal_test': dataset_rosenthal_test,
                                          'dataset_coefficient_of_endurance':dataset_coefficient_of_endurance})

@login_required
def physical_charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = PhysicalIndicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_pullups = PhysicalIndicator.objects.values('pullups').filter(user=id_user, date__range=[date_start, date_end])
        dataset_push_ups = PhysicalIndicator.objects.values('push_ups').filter(user=id_user, date__range=[date_start, date_end])
        dataset_sit_up = PhysicalIndicator.objects.values('sit_up').filter(user=id_user, date__range=[date_start, date_end])
        dataset_long_jump = PhysicalIndicator.objects.values('long_jump').filter(user=id_user,date__range=[date_start, date_end])
        dataset_acceleration = PhysicalIndicator.objects.values('acceleration').filter(user=id_user,date__range=[date_start, date_end])
        dataset_six_minute_run = PhysicalIndicator.objects.values('six_minute_run').filter(user=id_user,date__range=[date_start, date_end])
        dataset_shuttle_run = PhysicalIndicator.objects.values('shuttle_run').filter(user=id_user,date__range=[date_start, date_end])
        dataset_bridge = PhysicalIndicator.objects.values('bridge').filter(user=id_user,date__range=[date_start, date_end])
        dataset_twine = PhysicalIndicator.objects.values('twine').filter(user=id_user,date__range=[date_start, date_end])
        dataset_blow_strength = PhysicalIndicator.objects.values('blow_strength').filter(user=id_user,date__range=[date_start, date_end])
        dataset_endurance = PhysicalIndicator.objects.values('endurance').filter(user=id_user,date__range=[date_start, date_end])
        dataset_flexibility = PhysicalIndicator.objects.values('flexibility').filter(user=id_user,date__range=[date_start, date_end])
        dataset_coordination = PhysicalIndicator.objects.values('coordination').filter(user=id_user,date__range=[date_start, date_end])
        dataset_physical_fitness = PhysicalIndicator.objects.values('physical_fitness').filter(user=id_user,date__range=[date_start, date_end])
    else:
        formdate = ChartForm(post_request_chart)
        dataset_date = ['']
        dataset_pullups = []
        dataset_push_ups = []
        dataset_sit_up = []
        dataset_long_jump = []
        dataset_acceleration = []
        dataset_six_minute_run = []
        dataset_shuttle_run = []
        dataset_bridge = []
        dataset_twine = []
        dataset_blow_strength = []
        dataset_endurance = []
        dataset_flexibility = []
        dataset_coordination = []
        dataset_physical_fitness = []

    return render(request, 'charts/physical_charts.html', {'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_pullups':dataset_pullups,
                                          'dataset_push_ups':dataset_push_ups,
                                          'dataset_long_jump': dataset_long_jump,
                                          'dataset_acceleration': dataset_acceleration,
                                          'dataset_six_minute_run': dataset_six_minute_run,
                                          'dataset_shuttle_run': dataset_shuttle_run,
                                          'dataset_bridge': dataset_bridge,
                                          'dataset_twine': dataset_twine,
                                          'dataset_blow_strength': dataset_blow_strength,
                                                           'dataset_endurance': dataset_endurance,
                                                           'dataset_flexibility': dataset_flexibility,
                                                           'dataset_coordination': dataset_coordination,
                                                           'dataset_physical_fitness': dataset_physical_fitness,
                                                           'dataset_sit_up':dataset_sit_up})
@login_required
def tactical_charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = TacticaIndicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_versatility_technical_actions = TacticaIndicator.objects.values('versatility_technical_actions').filter(user=id_user, date__range=[date_start, date_end])
        dataset_attack_efficiency = TacticaIndicator.objects.values('attack_efficiency').filter(user=id_user, date__range=[date_start, date_end])
        dataset_protective_actions = TacticaIndicator.objects.values('protective_actions').filter(user=id_user, date__range=[date_start, date_end])

        dataset_warfare_ratio = TacticaIndicator.objects.values('warfare_ratio').filter(user=id_user, date__range=[date_start, date_end])
        dataset_performance_ratio = TacticaIndicator.objects.values('performance_ratio').filter(user=id_user, date__range=[date_start, date_end])
        dataset_technical_readiness = TacticaIndicator.objects.values('technical_readiness').filter(user=id_user, date__range=[date_start, date_end])
        dataset_tactical_action = TacticaIndicator.objects.values('tactical_action').filter(user=id_user, date__range=[date_start, date_end])
        dataset_versatility_actions = TacticaIndicator.objects.values('versatility_actions').filter(user=id_user, date__range=[date_start, date_end])
        dataset_chosen_tactics = TacticaIndicator.objects.values('chosen_tactics').filter(user=id_user, date__range=[date_start, date_end])
        dataset_adjustment_factor = TacticaIndicator.objects.values('adjustment_factor').filter(user=id_user, date__range=[date_start, date_end])
        dataset_preparatory_actions = TacticaIndicator.objects.values('preparatory_actions').filter(user=id_user, date__range=[date_start, date_end])
        dataset_situational_actions = TacticaIndicator.objects.values('situational_actions').filter(user=id_user, date__range=[date_start, date_end])
        dataset_scope_tactical_action = TacticaIndicator.objects.values('scope_tactical_action').filter(user=id_user, date__range=[date_start, date_end])

    else:
        formdate = ChartForm(post_request_chart)
        dataset_date = ['']
        dataset_versatility_technical_actions = []
        dataset_attack_efficiency = []
        dataset_protective_actions = []
        dataset_warfare_ratio = []
        dataset_performance_ratio = []
        dataset_technical_readiness = []
        dataset_tactical_action = []
        dataset_versatility_actions = []
        dataset_chosen_tactics = []
        dataset_adjustment_factor = []
        dataset_preparatory_actions = []
        dataset_situational_actions = []
        dataset_scope_tactical_action = []
    return render(request, 'charts/tactical_charts.html', {'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_versatility_technical_actions':dataset_versatility_technical_actions,
                                          'dataset_attack_efficiency':dataset_attack_efficiency,
                                          'dataset_warfare_ratio': dataset_warfare_ratio,
                                          'dataset_performance_ratio': dataset_performance_ratio,
                                          'dataset_technical_readiness': dataset_technical_readiness,
                                          'dataset_tactical_action': dataset_tactical_action,
                                          'dataset_versatility_actions': dataset_versatility_actions,
                                          'dataset_chosen_tactics': dataset_chosen_tactics,
                                          'dataset_adjustment_factor': dataset_adjustment_factor,
                                                           'dataset_preparatory_actions': dataset_preparatory_actions,
                                                           'dataset_situational_actions': dataset_situational_actions,
                                                           'dataset_scope_tactical_action': dataset_scope_tactical_action,
                                                           'dataset_protective_actions':dataset_protective_actions})

@login_required
def psy_charts(request):
    post_request_chart = request.session.get('post_request', None)
    if request.method == 'POST':
        request.session['post_request_chart'] = request.POST
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = PsyIndicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_thermometer_test = PsyIndicator.objects.values('thermometer_test').filter(user=id_user, date__range=[date_start, date_end])
        dataset_second_test = PsyIndicator.objects.values('second_test').filter(user=id_user, date__range=[date_start, date_end])
        dataset_emotional_stability = PsyIndicator.objects.values('emotional_stability').filter(user=id_user, date__range=[date_start, date_end])
        dataset_persistence_ratio = PsyIndicator.objects.values('persistence_ratio').filter(user=id_user, date__range=[date_start, date_end])
        dataset_courage_ratio = PsyIndicator.objects.values('courage_ratio').filter(user=id_user, date__range=[date_start, date_end])
    else:
        formdate = ChartForm(post_request_chart)
        dataset_date = ['']
        dataset_thermometer_test = []
        dataset_second_test = []
        dataset_emotional_stability = []
        dataset_persistence_ratio = []
        dataset_courage_ratio = []
    return render(request, 'charts/psy_charts.html', {'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_thermometer_test':dataset_thermometer_test,
                                          'dataset_second_test':dataset_second_test,
                                          'dataset_persistence_ratio': dataset_persistence_ratio,
                                          'dataset_courage_ratio': dataset_courage_ratio,
                                          'dataset_emotional_stability':dataset_emotional_stability})
