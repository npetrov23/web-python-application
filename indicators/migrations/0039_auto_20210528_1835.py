# Generated by Django 3.2 on 2021-05-28 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indicators', '0038_alter_grade_indicator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListIndicator',
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': 'Форматирование оценки', 'verbose_name_plural': 'Форматирование оценок'},
        ),
        migrations.AddField(
            model_name='grade',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Тренер'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='excellent',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Нижняя граница оценки "Отлично"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='excellent_border',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Верхняя граница оценки "Отлично"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='fine',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Нижняя граница оценки "Нормально"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='fine_border',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Верхняя граница оценки "Нормально"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='okay',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Нижняя граница оценки "Хорошо"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='okay_border',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Верхняя граница оценки "Хорошо"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='satisfactorily',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Нижняя граница оценки "Удовлитворительно"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='satisfactorily_border',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Верхняя граница оценки "Удовлитворительно"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='unsatisfactory',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Нижняя граница оценки "Неудовлетворительно"'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='unsatisfactory_border',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Верхняя граница оценки "Неудовлетворительно"'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='pulse_rate',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ЧПП'),
        ),
    ]
