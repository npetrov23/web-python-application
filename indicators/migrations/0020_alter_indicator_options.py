# Generated by Django 3.2 on 2021-05-01 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0019_alter_indicator_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicator',
            options={'permissions': (('can_add_func_indicator', 'can_view_list_sportsmen'),), 'verbose_name': 'Функциональная подготовленность', 'verbose_name_plural': 'Функциональная подготовленность'},
        ),
    ]