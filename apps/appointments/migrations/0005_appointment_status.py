# Generated by Django 3.2.11 on 2023-03-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_guest_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Abierto'), (2, 'Pendiente'), (3, 'Cancelado')], default=1),
        ),
    ]
