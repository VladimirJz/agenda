from xml.dom.minicompat import EmptyNodeList
from django.contrib import admin
from apps.company.models import Profile,Office,Employ
# Register your models here.

class EmployAdmin(admin.ModelAdmin):
    list_display=('Name','LastName','JobTittle','Office')


admin.site.register(Profile)
admin.site.register(Office)
admin.site.register(Employ,EmployAdmin)