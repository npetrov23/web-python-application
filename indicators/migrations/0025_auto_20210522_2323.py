# Generated by Django 3.2 on 2021-05-22 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indicators', '0024_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Список спортсменов у тренера', 'verbose_name_plural': 'Список спортсменов у тренера'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL, verbose_name='Принадлежит тренеру'),
        ),
    ]
