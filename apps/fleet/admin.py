from django.contrib import admin
from apps.fleet.models import Driver, Vehicle,VehicleClasification,VehicleManufacturer,Group,Issue
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display=('Clasification','Model','Year','VehiclePlate','Group')

class IssueAdmin(admin.ModelAdmin):
    list_display=('id','Vehicle','Date','Type','created_by','created_on')


admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleClasification)
admin.site.register(VehicleManufacturer)
admin.site.register(Group)
admin.site.register(Driver)
admin.site.register(Issue,IssueAdmin)
