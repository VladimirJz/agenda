# Generated by Django 3.2.11 on 2022-02-11 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DriverDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupName', models.CharField(help_text='Grupo vehicular', max_length=30, verbose_name='Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rigths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrafficIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleClasification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClasificationName', models.CharField(help_text='Clasificacion', max_length=30, verbose_name='Clasificación')),
                ('Code', models.CharField(help_text='Clave', max_length=10, null=True, verbose_name='Clave')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ManufacturerName', models.CharField(help_text='Fabricante', max_length=30, verbose_name='Fabricante')),
                ('Brand', models.CharField(help_text='Marca del vehiculo', max_length=30, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(help_text='Modelo del vehiculo', max_length=30, verbose_name='Modelo')),
                ('Year', models.SmallIntegerField(help_text='Año de fabricación', verbose_name='Año')),
                ('Color', models.CharField(help_text='Color del Vehiculo', max_length=30, verbose_name='Color')),
                ('FriendlyName', models.CharField(help_text='Identificador', max_length=30, verbose_name='Identificador')),
                ('VehiclePlate', models.CharField(help_text='Placas del vehiculo', max_length=12, verbose_name='Placas')),
                ('EnrollmentID', models.CharField(help_text='Matricula Vehicular', max_length=12, verbose_name='Matricula')),
                ('Transmission', models.SmallIntegerField(choices=[(1, 'Manual'), (2, 'Automática'), (3, 'CVT'), (4, 'Semiautomática'), (5, 'Dual-Cluth')], help_text='Tipo de transmisión', verbose_name='Transmision')),
                ('Motor', models.CharField(help_text='Detalle de motor', max_length=30, verbose_name='Motor')),
                ('SerialNumber', models.CharField(help_text='Numero de serie', max_length=30, verbose_name='NS')),
                ('MotorSerialNumber', models.CharField(help_text='Serie del motor', max_length=30, verbose_name='NS Motor')),
                ('Clasification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.vehicleclasification')),
                ('Group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.group')),
                ('Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleet.vehiclemanufacturer')),
            ],
        ),
    ]
