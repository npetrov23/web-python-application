# Generated by Django 3.2 on 2021-04-30 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0017_auto_20210430_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicator',
            options={'verbose_name': 'Функциональная подготовленность', 'verbose_name_plural': 'Функциональная подготовленность'},
        ),
        migrations.RemoveField(
            model_name='physicalindicator',
            name='scope_action',
        ),
    ]
