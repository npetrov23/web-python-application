# Generated by Django 3.2 on 2021-05-22 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0031_alter_profile_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='trainer',
        ),
    ]
