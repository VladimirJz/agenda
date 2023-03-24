from django.db import models

# Create your models here.
#
PRIORITIES=[(1,'Ugente'),(2,'Alta'),(3,'Normal')]
class Appointment(models.Model):
    subject=models.CharField(max_length=200,verbose_name='Asunto')
    date= models.DateField(verbose_name='Fecha')
    location=models.CharField(max_length=400,verbose_name='Ubicaciòn')
    
    
class Schedule(models.Model):
    start=models.TimeField(verbose_name='Desde')
    end=models.DateField(verbose_name='Hasta:')
    priority=models.SmallIntegerField(choices=PRIORITIES)
    
