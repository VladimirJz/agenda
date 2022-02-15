from django.contrib import admin
from apps.fleet.models import Vehicle,VehicleClasification,VehicleManufacturer,Group
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(VehicleClasification)
admin.site.register(VehicleManufacturer)
admin.site.register(Group)
