from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Indicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива', default=timezone.now)
    pulse_rate = models.IntegerField(verbose_name='ЧСС', null=True, blank=True, default=0)
    index_of_rufe = models.IntegerField(verbose_name='Проба Руффье', null=True, blank=True, default=0)
    coefficient_of_endurance = models.FloatField(verbose_name='Коэффициент выносливости',null=True, blank=True, default=0)
    blood_circulation = models.IntegerField(verbose_name='Коэффициент экономичности кровообращения',null=True, blank=True, default=0)
    orthostatic_test = models.FloatField(verbose_name='Ортостатическая проба',null=True, blank=True, default=0)
    clinostatic_test = models.FloatField(verbose_name='Клиностатическая проба',null=True, blank=True, default=0)
    rosenthal_test = models.IntegerField(verbose_name='Проба Розенталя',null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Функциональная подготовленность'
        verbose_name_plural = 'Функциональная подготовленность'
        unique_together = (('user', 'date'))


class PhysicalIndicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива', default=timezone.now)
    pullups = models.IntegerField(verbose_name='Подтягивания', null=True, blank=True, default=0)
    push_ups = models.IntegerField(verbose_name='Отжимания', null=True, blank=True, default=0)
    sit_up = models.IntegerField(verbose_name='Пресс "складка"', null=True, blank=True, default=0)
    long_jump = models.IntegerField(verbose_name='Прыжок в длину с места', null=True, blank=True, default=0)
    acceleration = models.FloatField(verbose_name='Ускорение 100м (c)',null=True, blank=True, default=0)
    six_minute_run = models.IntegerField(verbose_name='6-ти минутный бег (м)', null=True, blank=True, default=0)
    shuttle_run = models.IntegerField(verbose_name='Челночный бег 4х9м (с)', null=True, blank=True, default=0)
    bridge = models.IntegerField(verbose_name='"Мостик" (см)', null=True, blank=True, default=0)
    twine = models.IntegerField(verbose_name='"Шпагат" (см)', null=True, blank=True, default=0)
    blow_strength = models.FloatField(verbose_name='Сила ударов (%)',null=True, blank=True, default=0)
    endurance = models.FloatField(verbose_name='Выносливость (%)',null=True, blank=True, default=0)
    flexibility = models.FloatField(verbose_name='Гибкость (%)',null=True, blank=True, default=0)
    coordination = models.FloatField(verbose_name='Ккс (%)',null=True, blank=True, default=0)
    physical_fitness = models.FloatField(verbose_name='КсФП (%)',null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Физическая подготовленность'
        verbose_name_plural = 'Физическая подготовленность'
        unique_together = (('user','date'))


class TacticaIndicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива', default=timezone.now)
    versatility_technical_actions = models.IntegerField(verbose_name='Коэффициент объема технических действий',
                                                        null=True, blank=True, default=0)
    attack_efficiency = models.IntegerField(verbose_name='Коэффициент эффективности атакующих действий', null=True,
                                            blank=True, default=0)
    protective_actions = models.IntegerField(verbose_name='Коэффициент эффективности защитных действий', null=True,
                                             blank=True, default=0)
    warfare_ratio = models.IntegerField(verbose_name='Коэффициент эффективности боевых действий', null=True, blank=True, default=0)
    performance_ratio = models.FloatField(verbose_name='Коэффициент результативности',null=True, blank=True, default=0)
    technical_readiness = models.IntegerField(verbose_name='Техническая подготовленность', null=True, blank=True, default=0)
    tactical_action = models.IntegerField(verbose_name='Тактическая подготовленность', null=True, blank=True, default=0)
    versatility_actions = models.IntegerField(verbose_name='Разносторонность тактических действий', null=True, blank=True, default=0)
    chosen_tactics = models.IntegerField(verbose_name='Коэффициент избранной тактики', null=True, blank=True, default=0)
    adjustment_factor = models.FloatField(verbose_name='Коэффициент перестройки тактики',null=True, blank=True, default=0)
    preparatory_actions = models.FloatField(verbose_name='Коэффициент подготовительных тактических действий',null=True, blank=True, default=0)
    situational_actions = models.IntegerField(verbose_name='Коэффициент ситуативных тактических действий', null=True, blank=True, default=0)
    scope_tactical_action = models.IntegerField(verbose_name='Коэффициент объема тактических действий', null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Тактическая подготовленность'
        verbose_name_plural = 'Тактическая подготовленность'
        unique_together = (('user','date'))


class PsyIndicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Спортсмен')
    date = models.DateField(verbose_name='Дата норматива', default=timezone.now)
    thermometer_test = models.FloatField(verbose_name='Тест "Градусник"', null=True, blank=True, default=0)
    second_test = models.FloatField(verbose_name='Тест "10 секунд"', null=True, blank=True, default=0)
    emotional_stability = models.FloatField(verbose_name='Коэффициент эмоциональной устойчивости', null=True,
                                            blank=True, default=0)
    persistence_ratio = models.FloatField(verbose_name='Коэффициент настойчивости', null=True, blank=True, default=0)
    courage_ratio = models.FloatField(verbose_name='Коэффициент смелости', null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1})'.format(str(self.user),str(self.date))

    class Meta:
        verbose_name = 'Психологическая подготовленность'
        verbose_name_plural = 'Психологическая подготовленность'
        unique_together = (('user','date'))


class Grade(models.Model):
    indicator = models.CharField(verbose_name='Статистический показатель', max_length=256, null=True, blank=True, default='ЧПП')
    category = models.CharField(verbose_name='Категория', max_length=256)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Тренер', null=True, blank=True)
    excellent_border = models.IntegerField(verbose_name='Верхняя граница оценки "Отлично"', null=True, blank=True, default=0)
    excellent = models.IntegerField(verbose_name='Нижняя граница оценки "Отлично"', null=True, blank=True, default=0)
    okay_border = models.IntegerField(verbose_name='Верхняя граница оценки "Хорошо"', null=True, blank=True, default=0)
    okay = models.IntegerField(verbose_name='Нижняя граница оценки "Хорошо"', null=True, blank=True, default=0)
    fine_border = models.IntegerField(verbose_name='Верхняя граница оценки "Нормально"', null=True, blank=True, default=0)
    fine = models.IntegerField(verbose_name='Нижняя граница оценки "Нормально"', null=True, blank=True, default=0)
    satisfactorily_border = models.IntegerField(verbose_name='Верхняя граница оценки "Удовлитворительно"', null=True, blank=True, default=0)
    satisfactorily = models.IntegerField(verbose_name='Нижняя граница оценки "Удовлитворительно"', null=True, blank=True, default=0)
    unsatisfactory_border = models.IntegerField(verbose_name='Верхняя граница оценки "Неудовлетворительно"', null=True, blank=True, default=0)
    unsatisfactory = models.IntegerField(verbose_name='Нижняя граница оценки "Неудовлетворительно"', null=True, blank=True, default=0)

    def __str__(self):
        return '{0} ({1}), Тренер - {2}'.format(str(self.indicator), str(self.category), str(self.trainer))

    class Meta:
        verbose_name = 'Форматирование оценки'
        verbose_name_plural = 'Форматирование оценок'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Спортсмен', related_name='profile')
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Относится к тренеру', related_name='trener', null=True,blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Список спортсменов у тренера'
        verbose_name_plural = 'Список спортсменов у тренера'

def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()