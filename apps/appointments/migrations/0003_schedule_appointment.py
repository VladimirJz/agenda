# Generated by Django 3.2.11 on 2023-03-27 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20230327_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointments.appointment'),
        ),
    ]
