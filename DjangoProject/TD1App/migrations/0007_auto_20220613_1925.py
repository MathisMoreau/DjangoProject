# Generated by Django 3.1.14 on 2022-06-13 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TD1App', '0006_auto_20220613_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infra',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.TextField(max_length=20)),
                ('nb_machines', models.IntegerField(max_length=10)),
                ('Responsable', models.TextField(max_length=20)),
                ('entretien', models.DateField(default=datetime.datetime(2022, 6, 13, 19, 24, 56, 589333))),
            ],
        ),
        migrations.RemoveField(
            model_name='machine',
            name='mach',
        ),
        migrations.AddField(
            model_name='machine',
            name='machine',
            field=models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'MAc - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines '), ('Switch', 'Switch To maintains and connect servers'), ('Router', 'Router To connect internet')], default='PC', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 19, 24, 56, 564166)),
        ),
    ]
