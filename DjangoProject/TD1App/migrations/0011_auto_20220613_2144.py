# Generated by Django 3.1.14 on 2022-06-13 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TD1App', '0010_auto_20220613_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infra',
            name='entretien',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 21, 44, 7, 343164)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 21, 44, 7, 320714)),
        ),
    ]
