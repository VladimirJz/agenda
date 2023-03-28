from django.db import models
from django.urls import reverse
# Create your models here.
#
PRIORITIES=[(1,'Ugente'),(2,'Alta'),(3,'Normal')]
STATUS=[(1,'Abierto'),(2,'Pendiente'),(3,'Cancelado')]
class Appointment(models.Model):
    subject=models.CharField(max_length=200,verbose_name='Asunto')
    date= models.DateField(verbose_name='Fecha')
    location=models.CharField(max_length=400,verbose_name='Ubicaciòn')
    status=models.SmallIntegerField(choices=STATUS,default=1)
    start=models.TimeField(verbose_name='Hora de Inicio',null=True)
    end=models.TimeField(verbose_name='Hora fin:',null=True)
    priority=models.SmallIntegerField(choices=PRIORITIES,null=True)
    employ_id=models.IntegerField(verbose_name='Número de empleado',null=True,blank=True)  
    employ_name=models.CharField(max_length=50,verbose_name='Nombre', null=True)
    employ_title=models.CharField(max_length=30,verbose_name='Puesto',null=True)
    notes=models.TextField(null=True,blank=True)
    update_on=models.DateTimeField(auto_now=True)
    user_id=models.IntegerField(default=0,null=True)

    def __str__(self) -> str:
        return self.subject
    class Meta:
        db_table = "appointments_data"
        verbose_name_plural = "appointments"

    def get_absolute_url(self):
        return reverse('home')