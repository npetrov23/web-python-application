# Generated by Django 3.2 on 2021-06-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0039_auto_20210528_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='pulse_rate',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ЧСС'),
        ),
    ]
