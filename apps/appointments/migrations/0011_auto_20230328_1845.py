# Generated by Django 3.2.11 on 2023-03-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0010_auto_20230328_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end',
            field=models.TimeField(null=True, verbose_name='Hora fin:'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start',
            field=models.TimeField(null=True, verbose_name='Hora de Inicio'),
        ),
    ]
