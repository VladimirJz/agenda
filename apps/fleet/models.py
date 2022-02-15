from sre_parse import Verbose
from django.db import models

#Catalogos
TRANSMISSIONS=[(1,'Manual'),(2,'Automática'),(3,'CVT'),(4,'Semiautomática'),(5,'Dual-Cluth')]
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

class Vehicle(models.Model):
    Manufacturer=models.ForeignKey(VehicleManufacturer,on_delete=models.SET_NULL,null=True)
    Clasification=models.ForeignKey(VehicleClasification,on_delete=models.SET_NULL,null=True)
    Model=models.CharField(max_length=30,help_text='Modelo del vehiculo',verbose_name='Modelo')
    Year=models.SmallIntegerField(help_text='Año de fabricación',verbose_name='Año')
    Color=models.CharField(max_length=30,help_text='Color del Vehiculo',verbose_name='Color')
    FriendlyName=models.CharField(max_length=30,help_text='Identificador',verbose_name='Identificador')
    VehiclePlate=models.CharField(max_length=12,help_text='Placas del vehiculo',verbose_name='Placas')
    EnrollmentID=models.CharField(max_length=12,help_text='Matricula Vehicular',verbose_name='Matricula')
    Transmission=models.SmallIntegerField(choices=TRANSMISSIONS,help_text='Tipo de transmisión',verbose_name='Transmision')
    Motor=models.CharField(max_length=30,help_text='Detalle de motor',verbose_name='Motor')
    SerialNumber=models.CharField(max_length=30,help_text='Numero de serie',verbose_name='NS')
    MotorSerialNumber=models.CharField(max_length=30,help_text='Serie del motor',verbose_name='NS Motor')
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
    pass
class Agency(models.Model):
    pass
class Issue(models.Model):
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
    

