# Generated by Django 5.1.1 on 2024-10-01 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('date_creation', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Registro')),
                ('date_updated', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'ordering': ['id'],
            },
        ),
    ]
