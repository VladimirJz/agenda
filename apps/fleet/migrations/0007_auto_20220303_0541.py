# Generated by Django 3.2.11 on 2022-03-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0006_auto_20220223_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuelsupply',
            old_name='GaugeFuel',
            new_name='FuelReading',
        ),
        migrations.RenameField(
            model_name='fuelsupply',
            old_name='Odometer',
            new_name='TraveledReading',
        ),
        migrations.AlterField(
            model_name='fuelsupply',
            name='Quantity',
            field=models.PositiveSmallIntegerField(default=0, help_text='Unidades disponibles', verbose_name='Cantidad'),
        ),
    ]