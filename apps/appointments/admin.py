from django.contrib import admin
from  .models import Schedule,Appointment,Guest
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Schedule)
admin.site.register(Guest)