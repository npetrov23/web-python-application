# Generated by Django 3.2 on 2021-04-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0007_alter_indicator_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
