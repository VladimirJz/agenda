# Generated by Django 3.2.11 on 2022-03-03 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0007_auto_20220303_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FuelQuantity', models.PositiveIntegerField(help_text='Cantidad de Combustible', verbose_name='Combustible')),
                ('StartDate', models.DateField(help_text='Inicio de medición', verbose_name='Inicio')),
                ('EndDate', models.DateField(help_text='Final de medición', verbose_name='Fin')),
                ('InitialTravelReading', models.PositiveIntegerField(help_text='Lectura inicial del odometro', verbose_name='Lectura inicial')),
                ('FinalTravelReading', models.PositiveIntegerField(help_text='Lectura final del odometro', verbose_name='Lectura final')),
                ('FuelEfficiency', models.DecimalField(decimal_places=2, help_text='Rendimiento del combustible', max_digits=8, verbose_name='Eficiencia')),
                ('Driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.driver')),
                ('FuelSupply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.fuelsupply')),
            ],
        ),
    ]
