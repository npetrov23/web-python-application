from django.contrib.auth.models import User
from django.db import models

class Indicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива',default='2012-04-12')
    pulse_rate = models.IntegerField(verbose_name='ЧПП - в покое', null=True, blank=True, default=0)
    index_of_rufe = models.IntegerField(verbose_name='Проба Руффье', null=True, blank=True, default=0)
    coefficient_of_endurance = models.FloatField(verbose_name='Коэффициент выносливости',null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Физиологическая подготовленность'
        verbose_name_plural = 'Физиологическая подготовленность'
        unique_together = (('user','date'))


class PhysicalIndicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива',default='2012-04-12')
    pullups = models.IntegerField(verbose_name='Подтягивания', null=True, blank=True, default=0)
    push_ups = models.IntegerField(verbose_name='Отжимания', null=True, blank=True, default=0)
    sit_up = models.IntegerField(verbose_name='Пресс "складка"', null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Физическая подготовленность'
        verbose_name_plural = 'Физическая подготовленность'
        unique_together = (('user','date'))


class TacticaIndicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива',default='2012-04-12')
    versatility_technical_actions = models.IntegerField(verbose_name='Коэффициент объема технических действий',
                                                        null=True, blank=True, default=0)
    attack_efficiency = models.IntegerField(verbose_name='Коэффициент эффективности атакующих действий', null=True,
                                            blank=True, default=0)
    protective_actions = models.IntegerField(verbose_name='Коэффициент эффективности защитных действий', null=True,
                                             blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Тактическая подготовленность'
        verbose_name_plural = 'Тактическая подготовленность'
        unique_together = (('user','date'))


class PsyIndicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива',default='2012-04-12')
    thermometer_test = models.FloatField(verbose_name='Тест "Градусник"', null=True, blank=True, default=0)
    second_test = models.FloatField(verbose_name='Тест "10 секунд"', null=True, blank=True, default=0)
    emotional_stability = models.FloatField(verbose_name='Коэффициент эмоциональной устойчивости', null=True,
                                            blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Психологическая подготовленность'
        verbose_name_plural = 'Психологическая подготовленность'
        unique_together = (('user','date'))
