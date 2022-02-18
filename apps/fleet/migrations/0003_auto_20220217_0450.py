# Generated by Django 3.2.11 on 2022-02-17 04:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fleet', '0002_auto_20220216_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime.now, help_text='Fecha del Evento', verbose_name='Fecha')),
                ('Time', models.TimeField(blank=True, default=datetime.datetime.now, help_text='Hora del evento', verbose_name='Hora')),
                ('Type', models.SmallIntegerField(choices=[(1, 'Itinerario de Viaje'), (2, 'Suministro de Combustible'), (3, 'Suministro interno'), (4, 'Mantenimiento'), (5, 'Hecho de transito'), (6, 'Reporte de Falla')], default=1, help_text='Tipo de evento', null=True, verbose_name='Tipo')),
                ('Description', models.CharField(blank=True, help_text='Descripción del evento', max_length=100, verbose_name='Descripción')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('Driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.driver')),
                ('Vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.vehicle')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Supply',
            new_name='InternalSupply',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='Driver',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='Vehicle',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='IssueType',
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
    ]