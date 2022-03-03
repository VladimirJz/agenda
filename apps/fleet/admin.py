from django.contrib import admin
from apps.fleet.models import FUEL_TYPE, Driver, FuelSupply, Supplie, Supply, Vehicle,VehicleClasification,VehicleManufacturer,Group,Event
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display=('Clasification','Model','Year','VehiclePlate','Group')

class EventAdmin(admin.ModelAdmin):
    list_display=('id','Vehicle','Date','Type','created_by','created_on')

class FuelSupplyAdmin(admin.ModelAdmin):
    list_display=('id','Type')

admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleClasification)
admin.site.register(VehicleManufacturer)
admin.site.register(Group)
admin.site.register(Driver)
admin.site.register(Supplie)
admin.site.register(Supply)
admin.site.register(FuelSupply,FuelSupplyAdmin)
admin.site.register(Event,EventAdmin)
