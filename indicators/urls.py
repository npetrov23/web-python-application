from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.new_indicator, name='new'),
    url(r'^physical/new/$', views.new_physical_indicator, name='physical_new'),
    url(r'^tactical/new/$', views.new_tactical_indicator, name='tactical_new'),
    url(r'^psychological/new/$', views.new_psy_indicator, name='psychological_new'),

    url(r'^$', views.change_user, name='index'),
    url(r'^physical/$', views.physical_indicator, name='physical'),
    url(r'^tactical/$', views.tactical_indicator, name='tactical'),
    url(r'^psychological/$', views.psy_indicator, name='psy'),

    url(r'^charts/$', views.charts, name='charts'),
    url(r'^physical/charts/$', views.physical_charts, name='physical_charts'),
    url(r'^tactical/charts/$', views.tactical_charts, name='tactical_charts'),
    url(r'^psychological/charts/$', views.psy_charts, name='psy_charts'),

    url(r'^grade/$', views.grade_formatting, name='grade'),

    url('register/', views.register, name='register'),
    url('new_sportsmen/', views.register_sportsmen, name='register_sportsmen'),
]