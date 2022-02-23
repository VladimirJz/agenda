# Generated by Django 3.2.11 on 2022-02-23 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0005_auto_20220217_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskName', models.CharField(help_text='Actividad o rutina de mantenimiento', max_length=30, verbose_name='Actividad')),
                ('Type', models.SmallIntegerField(choices=[(1, 'Preventivo'), (2, 'Correctivo')], default=1, help_text='Tipo de mantenimiento', verbose_name='Tipo')),
                ('Schedulable', models.BooleanField(default=False, help_text='¿Se programa periodicamente?', verbose_name='Programable?')),
                ('Description', models.CharField(help_text='Descripción', max_length=300, verbose_name='Descripción')),
            ],
        ),
        migrations.AddField(
            model_name='maintenance',
            name='Event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.event'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='ArrestedDriver',
            field=models.BooleanField(default=False, help_text='Fue detenido el conductor?', verbose_name='Detenido?'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='BetweenStreet',
            field=models.TextField(help_text='Entrecalles', max_length=300, null=True, verbose_name='Entrecalles'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='City',
            field=models.TextField(help_text='Ciudad', max_length=100, null=True, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='Descrition',
            field=models.TextField(help_text='Descripciòn del incidente', max_length=300, null=True, verbose_name='Descripciòn'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='DisableVehicle',
            field=models.BooleanField(default=False, help_text='Fue inhabilitado el vehiculo?', verbose_name='Vehiculo deshabilitado?'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='Event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.event'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='InjuredPeople',
            field=models.BooleanField(default=False, help_text='Existen personsas lesionadas?', verbose_name='Lesiones?'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='InsuranceReportID',
            field=models.TextField(help_text='ID de Reporte Aseguradora', max_length=10, null=True, verbose_name='Reporte Aseguradora'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='Severity',
            field=models.SmallIntegerField(choices=[(1, 'Estetico'), (2, 'Menor'), (3, 'Moderada'), (4, 'Mayor'), (5, 'Crítica')], null=True),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='Street',
            field=models.TextField(help_text='Calle', max_length=100, null=True, verbose_name='Calle'),
        ),
        migrations.AddField(
            model_name='trafficincident',
            name='TicketID',
            field=models.CharField(help_text='ID del Ticket de transito', max_length=20, null=True, verbose_name='Folio de Multa'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='Status',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Disponible'), (2, 'En ruta'), (3, 'En reparación / Detenido'), (4, 'Baja')], default=1),
        ),
        migrations.CreateModel(
            name='MaintenanceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maintenance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.maintenance')),
                ('Task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.maintenancetask')),
            ],
        ),
    ]