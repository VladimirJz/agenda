from django.contrib import admin
from apps.fleet.models import Vehicle,VehicleClasification,VehicleManufacturer,Group
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display=('Clasification','Model','Year','VehiclePlate','Group')




admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleClasification)
admin.site.register(VehicleManufacturer)
admin.site.register(Group)
