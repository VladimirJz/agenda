from django.contrib import admin
from django.urls import path
from apps.fleet.views import EventCreateView, dashboard,index,FuelSupplyCreateView

# el name de cada path se usa para generar el breadcrumb, por lo que debe
# respetar el patron anidado de las vistas, por ejemplo:
#  flota_vehiculo_nuevo 
# genera el un breadcrumb de tipo Flota > Vehiculo > Nuevo
# donde Nuevo es la vista actual es decir
# fleet/vehicle/new

urlpatterns=[
            path('/',dashboard.as_view(),name='flota'),
            path('vehicles/',index.as_view(),name='flota_vehiculos'),
            path('vehicle/event/',EventCreateView.as_view(),name='event_new'),
            path('vehicle/fuelsupply/<int:pk>',FuelSupplyCreateView.as_view(),name='fuel_supply')
            ]



