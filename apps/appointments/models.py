from django.db import models

# Create your models here.
#
PRIORITIES=[(1,'Ugente'),(2,'Alta'),(3,'Normal')]
STATUS=[(1,'Abierto'),(2,'Pendiente'),(3,'Cancelado')]
class Appointment(models.Model):
    subject=models.CharField(max_length=200,verbose_name='Asunto')
    date= models.DateField(verbose_name='Fecha')
    location=models.CharField(max_length=400,verbose_name='Ubicaciòn')
    notes=models.TextField(null=True,blank=True)
    status=models.SmallIntegerField(choices=STATUS,default=1)
    def __str__(self) -> str:
        return self.subject
    
    
class Schedule(models.Model):
    appointment=models.OneToOneField(Appointment,related_name='schedule',on_delete=models.SET_NULL,null=True)
    start=models.DateTimeField(verbose_name='Desde')
    end=models.DateTimeField(verbose_name='Hasta:')
    priority=models.SmallIntegerField(choices=PRIORITIES)
    def __str__(self) -> str:
        return str(self.start.hour) +'-' + str(self.end.hour)

class Guest(models.Model):
    appointment=models.OneToOneField(Appointment,related_name='guest',on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=50,verbose_name='Nombre')
    title=models.CharField(max_length=30,verbose_name='Puesto')  
    def __str__(self) -> str:
        return self.name 
