# Generated by Django 3.2 on 2021-05-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0025_auto_20210522_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sportsmen',
            new_name='user',
        ),
    ]
