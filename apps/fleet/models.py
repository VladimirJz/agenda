from datetime import datetime
from sqlite3 import Date
from sre_parse import Verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.core.exceptions import ValidationError

from apps.company.models import Employ






#Catalogos
TRANSMISSION_TYPE=[(1,'Manual'),(2,'Automática'),(3,'CVT'),(4,'Semiautomática'),(5,'Dual-Cluth')]
EVENT_TYPE=[(1,'Itinerario de Viaje'),(2,'Suministro de Combustible'),(3,'Suministro interno'),(4,'Mantenimiento'),(5,'Hecho de transito'),(6,'Reporte de Falla'),(7,'Asignación')]
FUEL_TYPE=[(1,'Gasolina'),(2,'Diesel')]
SEVERITY_TYPE=[(1,'Estetico'),(2,'Menor'),(3,'Moderada'),(4,'Mayor'),(5,'Crítica')]
MAINTENANCE_TYPE=[(1,'Preventivo'),(2,'Correctivo')]
VEHICLE_STATUS=(1,'Disponible'),(2,'En ruta'), (3,'En reparación / Detenido'),(4,'Baja'),
# Create your models here.
class Group(models.Model):
    GroupName=models.CharField(max_length=30,help_text='Grupo vehicular',verbose_name='Grupo')
    def __str__(self):
        return self.GroupName


class DriverDocument(models.Model):
    pass
class DocumentType(models.Model):
    pass
class Driver(models.Model):
    Employ=models.ForeignKey(Employ,on_delete=models.SET_NULL,null=True)
    Comments=models.CharField(max_length=300,help_text='Comentarios sobre el conductor',verbose_name='Observaciones',blank=True,default='')

    def __str__(self):
        return str(self.Employ)

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

#TODO: agregar Medidad de uso (km/milla/hora) / medida de combustible
#TODO: Agregar el rendimiento ideal: l/Km
#TODO: Cambiar Year por Line, la linea del vehiculo, en lugar del año NO PROCEDE
#TODO: Se requiere una clase para controlar la distribuciòn de itinerarios de los vehiculos
#TODO: Gestionar el estatus del vehiculo (asignado/talller/fuera de servicio/disponible)
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
    FuelType=models.SmallIntegerField(choices=FUEL_TYPE,verbose_name='Tipo  ',help_text='Tipo de combustible',default=1)
    TankCapacity=models.PositiveIntegerField(verbose_name='Capacidad del tanque',help_text='Capacidad del tanque de combustible',null=True)
    SerialNumber=models.CharField(max_length=30,help_text='Numero de serie',verbose_name='NS')
    EngineSerialNumber=models.CharField(max_length=30,help_text='Serie del motor',verbose_name='NS Motor')
    Group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    Status=models.SmallIntegerField(choices=VEHICLE_STATUS,default=1,blank=True)
    update_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    update_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.FriendlyName
    def Options(self):
        return 'Detalles_Eliminar'
    def last_traveled_reading(self):   
        reading=FuelConsumption.objects.filter()

# TODO:el estado del vehiculo debe  llevar el registro de las condiciones generales
# observadas en el mismo desde la asignación del conductor, como el seguro, garantia,
# estado de leasing, etc.

class State(models.Model):
    Vehicle=models.OneToOneField(Vehicle,on_delete=models.SET_NULL,null=True)
    Driver=models.OneToOneField(Driver,on_delete=models.SET_NULL,null=True,related_name='his_driver',verbose_name='Conductor asignado')
    update_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    update_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    pass


class VehicleDocument(models.Model):
    pass

class Agency(models.Model):
    pass
class Event(models.Model):
    Date=models.DateField(verbose_name='Fecha',help_text='Fecha del Evento',auto_now=False,default=datetime.now)
    Time=models.TimeField(verbose_name='Hora', help_text='Hora del evento',default=datetime.now,blank=True)
    #Classification=models.SmallIntegerField(choices=ISSUE_CLASS,help_text='Tipo de Evento',verbose_name='Evento')
    Type=models.SmallIntegerField(choices=EVENT_TYPE,help_text='Tipo de evento',verbose_name='Tipo',default=1,null=True)
    Description=models.CharField(max_length=100, help_text='Descripción del evento',verbose_name='Descripción',blank=True)
    Vehicle=models.ForeignKey(Vehicle,on_delete=models.SET_NULL,null=True)
    Driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True,verbose_name='Conductor')
    update_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    update_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return str(self.Type) + ' ' + self.Description + ' - ' + str(self.Vehicle)
# primary,secoundary ,info,sucess,warnig,Danger
    @property
    def level(self):
        switcher = {
                    1: "success",
                    2: "info",
                    3: "info",
                    4: "warning",
                    5: "danger",
                    6: "warning",
                    7: "secondary",
                }
        return switcher.get(self.Type, "info")

#    EVENT_TYPE=[(1,'Itinerario de Viaje'),(2,'Suministro de Combustible'),(3,'Suministro interno'),(4,'Mantenimiento'),(5,'Hecho de transito'),(6,'Reporte de Falla'),(7,'Asignación')]
    @property
    def icon(self):
            switcher = {
                        1: "fas fa-map-marked-alt",
                        2: "fa fa-gas-pump",
                        3: "fas fa-box-open",
                        4: "fas fa-wrench",
                        5: "fas fa-car-crash",
                        6: "far fa-lightbulb",
                        7: "fas fa-user-check",
                    }
            return switcher.get(self.Type, "far fa-lightbulb")
# El tipo puede ser una lista fija


# Tipos de  Eventos:

# catalogo interno configurable por la empresa
class Supplie(models.Model):
    SupplieName=models.CharField(max_length=30,verbose_name='Nombre',help_text='Nombre del suministro')
    Description=models.CharField(max_length=30,verbose_name='Descripción',help_text='Descripción del articulo')
    Stock=models.SmallIntegerField(verbose_name='Existencias',help_text='Unidades disponibles')
    CostPerUnit=models.DecimalField(decimal_places=2,max_digits=6, verbose_name='Costo por unidad',help_text='Costo por unidad',default=0.0)
    def __str__(self):
        return self.SupplieName


# Suministros internos para viaje
class Supply(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    Supplie=models.ForeignKey(Supplie,on_delete=models.SET_NULL,null=True)
    Quantity=models.PositiveSmallIntegerField(verbose_name='Cantidad',help_text='Cantidad')
    Cost=models.DecimalField(decimal_places=2,max_digits=6, verbose_name='Costo',help_text='Costo',default=0.0)
    def __str__(self):
        return str(self.Event) + ' - ' + str(self.Supplie)
  

# Suministro de Combustible
class FuelSupply(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    Type=models.SmallIntegerField(choices=FUEL_TYPE,verbose_name='Tipo',help_text='Tipo de combustible',default=1)
    FuelReading=models.PositiveSmallIntegerField(verbose_name='Indicador de combustible',help_text='Porcentaje de combustible en el Tanque',default=0)
    #FullTank=models.BooleanField(default=False,verbose_name='Tanque lleno?',help_text='Se llena el tanque con la carga de combustible')
    Quantity=models.PositiveSmallIntegerField(verbose_name='Cantidad',help_text='Unidades disponibles',default=0)
    CostPerUnit=models.DecimalField(decimal_places=2,max_digits=6, verbose_name='Costo por unidad',help_text='Costo por unidad',default=0.0)
    TraveledReading=models.PositiveIntegerField(verbose_name='Kilometraje.',help_text='Medición del odometro',default=0)
    Comments=models.CharField(max_length=300,verbose_name='Comentarios',help_text='Comentarios / Referencia',null=True)
    update_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    update_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def clean(self):
            if not(self.Quantity) > 1:
                raise ValidationError(
                    {'Quantity': "La cantidad no puede ser cero"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)



# Incidente de Trafico
class TrafficIncident(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    TicketID=models.CharField(max_length=20,verbose_name='Folio de Multa',help_text='ID del Ticket de transito',null=True)
    Descrition=models.TextField(max_length=300,verbose_name='Descripciòn',help_text='Descripciòn del incidente',null=True)
    City=models.TextField(max_length=100, verbose_name='Ciudad',help_text='Ciudad',null=True)
    Street=models.TextField(max_length=100,verbose_name='Calle',help_text='Calle',null=True)
    BetweenStreet=models.TextField(max_length=300,verbose_name='Entrecalles',help_text='Entrecalles',null=True)
    Severity=models.SmallIntegerField(choices=SEVERITY_TYPE,null=True)
    InsuranceReportID=models.TextField(max_length=10,verbose_name='Reporte Aseguradora',help_text='ID de Reporte Aseguradora',null=True)
    InjuredPeople=models.BooleanField(default=False,verbose_name='Lesiones?',help_text='Existen personsas lesionadas?')
    ArrestedDriver=models.BooleanField(default=False,verbose_name='Detenido?',help_text='Fue detenido el conductor?')
    DisableVehicle=models.BooleanField(default=False,verbose_name='Vehiculo deshabilitado?',help_text='Fue inhabilitado el vehiculo?')
    update_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    update_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)
# Asignaciòn
 
class Assignment(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    Driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True,verbose_name='Conductor asignado')
    FuelReading=models.PositiveSmallIntegerField(verbose_name='Indicador de combustible',help_text='Porcentaje de combustible en el Tanque',default=0)
    TraveledReading=models.PositiveIntegerField(verbose_name='Indicador de recorrido.',help_text='Medición del odometro',default=0)
    Comments=models.CharField(max_length=300,verbose_name='Comentarios',help_text='Comentarios / observaciones')
    update_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    update_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)



    def clean(self):
        pass

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


#
    pass

#Reportes 
class Issue(models.Model):
    pass

# Estos eventos se pueden relacional con una programación
# Mantenimiento (preventivo/Correctivo)
class MaintenanceTask(models.Model):
    TaskName=models.CharField(max_length=30,verbose_name='Actividad',help_text='Actividad o rutina de mantenimiento')
    Type=models.SmallIntegerField(choices=MAINTENANCE_TYPE,default=1,verbose_name='Tipo',help_text='Tipo de mantenimiento')
    Schedulable=models.BooleanField(default=False,verbose_name='Programable?',help_text='¿Se programa periodicamente?')
    Description=models.CharField(max_length=300,verbose_name='Descripción',help_text='Descripción')


class Maintenance(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    #Taller#Mecanico
    #
class MaintenanceDetail(models.Model):
    Maintenance=models.ForeignKey(Maintenance,on_delete=models.SET_NULL,null=True)
    Task=models.ForeignKey(MaintenanceTask,on_delete=models.SET_NULL,null=True)


    
class FuelConsumption(models.Model):
    FuelSupply=models.ForeignKey(FuelSupply,on_delete=models.SET_NULL,null=True)
    Driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True)

    FuelQuantity=models.PositiveIntegerField(verbose_name='Combustible', help_text='Cantidad de Combustible')
    StartDate=models.DateField(verbose_name='Inicio',help_text='Inicio de medición')
    EndDate=models.DateField(verbose_name='Fin',help_text='Final de medición',null=True )
    InitialTraveledReading=models.PositiveIntegerField(verbose_name='Lectura inicial',help_text='Lectura inicial del odometro')    
    FinalTraveledReading=models.PositiveIntegerField(verbose_name='Lectura final',help_text='Lectura final del odometro',null=True)    
    FuelEfficiency=models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Eficiencia',help_text='Rendimiento del combustible',null=True)
    #VehicleAvgFuelEfficiency=models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Eficiencia promedio',help_text='Rendimiento promedio de combustible')
    #DriverAvgFuelEfficiency=models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Eficiencia promedio',help_text='Rendimiento promedio de combustible')

    def __str__(self):
        return str(self.StartDate)
    
# Itinirario de Viaje
class Itinerary(models.Model):
    pass

# Derechos (alta /baja/ Vencimientos de Derechos / )
class Rigths(models.Model):
    pass


# # Historico
# class FuelPerformace(models.Model):
#     #Date=models.DateField(verbose_name='Fecha',help_text='Fecha')
#     #InitOdometer=models.
#     pass


    