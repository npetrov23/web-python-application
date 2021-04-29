
from django.shortcuts import render
from .forms import IndicatorForm, ChangeSportsmenForm, ChartForm, PhysicalIndicatorForm, PsyIndicatorForm, \
    TacticalIndicatorForm
from .models import Indicator



def change_user(request):
    pulse_rate = 0
    index_of_rufe = 0
    coefficient_of_endurance = 0
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        #if form.is_valid():
        if Indicator.objects.filter(user=request.POST.get('user')) and \
                Indicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            pulse_rate = Indicator.objects.filter(date=date,user=id_user).values_list('pulse_rate', flat=True)[0]
            index_of_rufe = Indicator.objects.filter(date=date,user=id_user).values_list('index_of_rufe', flat=True)[0]
            coefficient_of_endurance = Indicator.objects.filter(date=date,user=id_user).values_list('coefficient_of_endurance', flat=True)[0]
        #print('DATA',request.POST.get('date_year')+'-'+request.POST.get('dat_month')+'-'+request.POST.get('date_day'))
    else:
        form = ChangeSportsmenForm()
    return render(request,'index.html',{'form':form, 'pulse_rate': pulse_rate, 'index_of_rufe': index_of_rufe, 'coefficient_of_endurance': coefficient_of_endurance})

def new_indicator(request):
    if request.method == 'POST':
        form_new_indicator = IndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = IndicatorForm()
    return render(request, 'new_indicator.html', {'form_new_indicator':form_new_indicator})

def new_physical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PhysicalIndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PhysicalIndicatorForm()
    return render(request, 'new_physical_indicator.html', {'form_new_indicator':form_new_indicator})

def new_tactical_indicator(request):
    if request.method == 'POST':
        form_new_indicator = TacticalIndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = TacticalIndicatorForm()
    return render(request, 'new_tactical_indicator.html', {'form_new_indicator':form_new_indicator})

def new_psy_indicator(request):
    if request.method == 'POST':
        form_new_indicator = PsyIndicatorForm(request.POST)
        if form_new_indicator.is_valid():
            form_new_indicator.save()
    else:
        form_new_indicator = PsyIndicatorForm()
    return render(request, 'new_psy_indicator.html', {'form_new_indicator':form_new_indicator})

def physical_indicator(request):
    pullups = 0
    push_ups = 0
    sit_up = 0
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        #if form.is_valid():
        if Indicator.objects.filter(user=request.POST.get('user')) and \
                Indicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            pullups = Indicator.objects.filter(date=date,user=id_user).values_list('pullups', flat=True)[0]
            push_ups = Indicator.objects.filter(date=date,user=id_user).values_list('push_ups', flat=True)[0]
            sit_up = Indicator.objects.filter(date=date,user=id_user).values_list('sit_up', flat=True)[0]
        #print('DATA',request.POST.get('date_year')+'-'+request.POST.get('dat_month')+'-'+request.POST.get('date_day'))
    else:
        form = ChangeSportsmenForm()

    return render(request,'PhysicalTraining.html',{'form':form, 'pullups': pullups, 'push_ups': push_ups, 'sit_up': sit_up})

def tactical_indicator(request):
    versatility_technical_actions = 0
    attack_efficiency = 0
    protective_actions = 0
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        #if form.is_valid():
        if Indicator.objects.filter(user=request.POST.get('user')) and \
                Indicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            versatility_technical_actions = Indicator.objects.filter(date=date,user=id_user).values_list('versatility_technical_actions', flat=True)[0]
            attack_efficiency = Indicator.objects.filter(date=date,user=id_user).values_list('attack_efficiency', flat=True)[0]
            protective_actions = Indicator.objects.filter(date=date,user=id_user).values_list('protective_actions', flat=True)[0]
        #print('DATA',request.POST.get('date_year')+'-'+request.POST.get('dat_month')+'-'+request.POST.get('date_day'))
    else:
        form = ChangeSportsmenForm()
    return render(request,'TacticalTraining.html',{'form':form, 'versatility_technical_actions': versatility_technical_actions, 'attack_efficiency': attack_efficiency, 'protective_actions': protective_actions})

def psy_indicator(request):
    thermometer_test = 0
    second_test = 0
    emotional_stability = 0
    if request.method == 'POST':
        form = ChangeSportsmenForm(request.POST)
        #if form.is_valid():
        if Indicator.objects.filter(user=request.POST.get('user')) and \
                Indicator.objects.filter(date=str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))):
            id_user = request.POST.get('user')
            date = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))#Indicator.objects.filter(date=request.POST.get('date')).values_list('date', flat=True)[0]
            thermometer_test = Indicator.objects.filter(date=date,user=id_user).values_list('thermometer_test', flat=True)[0]
            second_test = Indicator.objects.filter(date=date,user=id_user).values_list('second_test', flat=True)[0]
            emotional_stability = Indicator.objects.filter(date=date,user=id_user).values_list('emotional_stability', flat=True)[0]
        #print('DATA',request.POST.get('date_year')+'-'+request.POST.get('dat_month')+'-'+request.POST.get('date_day'))
    else:
        form = ChangeSportsmenForm()
    return render(request,'PsychologicalTraining.html',{'form':form, 'thermometer_test': thermometer_test, 'second_test': second_test, 'emotional_stability': emotional_stability})

def charts(request):
    if request.method == 'POST':
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = Indicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_pulse_rate = Indicator.objects.values('pulse_rate').filter(user=id_user, date__range=[date_start, date_end])
        dataset_index_of_rufe = Indicator.objects.values('index_of_rufe').filter(user=id_user, date__range=[date_start, date_end])
        dataset_coefficient_of_endurance = Indicator.objects.values('coefficient_of_endurance').filter(user=id_user, date__range=[date_start, date_end])
        print(dataset_coefficient_of_endurance)
    else:
        formdate = ChartForm()
        dataset_date = ['']
        dataset_pulse_rate = []
        dataset_index_of_rufe = []
        dataset_coefficient_of_endurance = []
    return render(request, 'charts.html',{'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_pulse_rate':dataset_pulse_rate,
                                          'dataset_index_of_rufe':dataset_index_of_rufe,
                                          'dataset_coefficient_of_endurance':dataset_coefficient_of_endurance})

def physical_charts(request):
    if request.method == 'POST':
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = Indicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_pullups = Indicator.objects.values('pullups').filter(user=id_user, date__range=[date_start, date_end])
        dataset_push_ups = Indicator.objects.values('push_ups').filter(user=id_user, date__range=[date_start, date_end])
        dataset_sit_up = Indicator.objects.values('sit_up').filter(user=id_user, date__range=[date_start, date_end])
    else:
        formdate = ChartForm()
        dataset_date = ['']
        dataset_pullups = []
        dataset_push_ups = []
        dataset_sit_up = []
    return render(request, 'physical_charts.html',{'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_pullups':dataset_pullups,
                                          'dataset_push_ups':dataset_push_ups,
                                          'dataset_sit_up':dataset_sit_up})

def tactical_charts(request):
    if request.method == 'POST':
        id_user = request.POST.get('user')
        date_start = str(request.POST.get('date_year'))+'-'+str(request.POST.get('date_month'))+'-'+str(request.POST.get('date_day'))
        date_end = str(request.POST.get('end_date_year'))+'-'+str(request.POST.get('end_date_month'))+'-'+str(request.POST.get('end_date_day'))

        formdate = ChartForm(request.POST)
        dataset_date = Indicator.objects.values('date').filter(user=id_user,date__range=[date_start, date_end])
        dataset_versatility_technical_actions = Indicator.objects.values('versatility_technical_actions').filter(user=id_user, date__range=[date_start, date_end])
        dataset_attack_efficiency = Indicator.objects.values('attack_efficiency').filter(user=id_user, date__range=[date_start, date_end])
        dataset_protective_actions = Indicator.objects.values('protective_actions').filter(user=id_user, date__range=[date_start, date_end])
        print(dataset_versatility_technical_actions)
    else:
        formdate = ChartForm()
        dataset_date = ['']
        dataset_versatility_technical_actions = []
        dataset_attack_efficiency = []
        dataset_protective_actions = []
    return render(request, 'tactical_charts.html',{'formdate':formdate,
                                          'dataset_date':dataset_date,
                                          'dataset_versatility_technical_actions':dataset_versatility_technical_actions,
                                          'dataset_attack_efficiency':dataset_attack_efficiency,
                                          'dataset_protective_actions':dataset_protective_actions})
