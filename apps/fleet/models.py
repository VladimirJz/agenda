from datetime import datetime
from sqlite3 import Date
from sre_parse import Verbose
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User

from apps.company.models import Employ






#Catalogos
TRANSMISSION_TYPE=[(1,'Manual'),(2,'Automática'),(3,'CVT'),(4,'Semiautomática'),(5,'Dual-Cluth')]
ISSUE_TYPE=[(1,'Itinerario de Viaje'),(2,'Suministro de Combustible'),(3,'Suministro interno'),(4,'Mantenimiento'),(5,'Hecho de transito')]
# Create your models here.
class Group(models.Model):
    GroupName=models.CharField(max_length=30,help_text='Grupo vehicular',verbose_name='Grupo')
    def __str__(self):
        return self.GroupName

class VehicleClasification(models.Model):
    ClasificationName=models.CharField(max_length=30,help_text='Clasificacion',verbose_name='Clasificación')
    Code=models.CharField(max_length=20,help_text='Clave',verbose_name='Clave',null=True)
    
    def __str__(self):
        return self.ClasificationName



class VehicleManufacturer(models.Model):
    ManufacturerName=models.CharField(max_length=30,help_text='Fabricante',verbose_name='Fabricante')
    Brand=models.CharField(max_length=30,help_text='Marca del vehiculo',verbose_name='Marca')
    def __str__(self):
        return self.ManufacturerName + '-' + self.Brand


#TODO: agregar medida (km/milla) 
#TODO: Agregar el rendimiento ideal: l/Km
#TODO: Cambiar Year por Line, la linea del vehiculo, en lugar del año NO PROCEDE
#TODO: Se requiere una clase para controlar la distribuciòn de itinerarios de los vehiculos
#          issue-> Itinerary -> ScheduleItinerary(Global)

class Vehicle(models.Model):
    Manufacturer=models.ForeignKey(VehicleManufacturer,on_delete=models.SET_NULL,null=True)
    Clasification=models.ForeignKey(VehicleClasification,on_delete=models.SET_NULL,null=True)
    Model=models.CharField(max_length=30,help_text='Modelo del vehiculo',verbose_name='Modelo')
    Year=models.SmallIntegerField(help_text='Año de fabricación',verbose_name='Año')
    Color=models.CharField(max_length=30,help_text='Color del Vehiculo',verbose_name='Color')
    FriendlyName=models.CharField(max_length=30,help_text='Identificador',verbose_name='Identificador')
    VehiclePlate=models.CharField(max_length=12,help_text='Placas del vehiculo',verbose_name='Placas')
    EnrollmentID=models.CharField(max_length=12,help_text='Matricula Vehicular',verbose_name='Matricula')
    Transmission=models.SmallIntegerField(choices=TRANSMISSION_TYPE,help_text='Tipo de transmisión',verbose_name='Transmision')
    Motor=models.CharField(max_length=30,help_text='Detalle de motor',verbose_name='Motor')
    SerialNumber=models.CharField(max_length=30,help_text='Numero de serie',verbose_name='NS')
    EngineSerialNumber=models.CharField(max_length=30,help_text='Serie del motor',verbose_name='NS Motor')
    Group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.FriendlyName
    def Options(self):
        return 'Detalles_Eliminar'


class VehicleDocument(models.Model):
    pass
class DriverDocument(models.Model):
    pass
class DocumentType(models.Model):
    pass
class Driver(models.Model):
    Employ=models.ForeignKey(Employ,on_delete=models.SET_NULL,null=True)
    Comments=models.CharField(max_length=300,help_text='Comentarios sobre el conductor',verbose_name='Observaciones',blank=True,default='')

    def __str__(self):
        return str(self.Employ)

class Agency(models.Model):
    pass
class Issue(models.Model):
    Date=models.DateField(verbose_name='Fecha',help_text='Fecha del Evento',auto_now=False,default=datetime.now)
    Time=models.TimeField(verbose_name='Hora', help_text='Hora del evento',default=datetime.now,blank=True)
    #Classification=models.SmallIntegerField(choices=ISSUE_CLASS,help_text='Tipo de Evento',verbose_name='Evento')
    Type=models.SmallIntegerField(choices=ISSUE_TYPE,help_text='Tipo de evento',verbose_name='Tipo',default=1,null=True)
    Description=models.CharField(max_length=100,help_text='Descripción del evento',verbose_name='Descripción',blank=True)
    Vehicle=models.ForeignKey(Vehicle,on_delete=models.SET_NULL,null=True)
    Driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    pass
# El tipo puede ser una lista fija
class IssueType(models.Model):
    pass

# Tipos de  Eventos:
class Supply(models.Model):
    pass
class TrafficIncident(models.Model):
    pass
class Maintenance(models.Model):
    pass
class Itinerary(models.Model):
    pass

class Rigths(models.Model):
    pass
    

