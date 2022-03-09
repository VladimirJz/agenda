from django.contrib import admin
from django.urls import path
from apps.fleet.views import  FuelSupplyListView, dashboard,FuelSupplyCreateView,VehicleListView,VehicleAssignmentView,VehicleAssigmmentListView,VehicleDetailView

# el name de cada path se usa para generar el breadcrumb, por lo que debe
# respetar el patron anidado de las vistas, por ejemplo:
#  flota_vehiculo_nuevo 
# genera el un breadcrumb de tipo Flota > Vehiculo > Nuevo
# donde Nuevo es la vista actual es decir
# fleet/vehicle/new

urlpatterns=[
            path('',dashboard.as_view(),name='flota'),
            path('vehicles/',VehicleListView.as_view(),name='flota_vehiculos'),
            #path('vehicles/event/',EventCreateView_.as_view(),name='event_new'),
            path('vehicles/<int:pk>/fuelsupply',FuelSupplyCreateView.as_view(),name='flota_vehiculos_combustible'),
            #path('vehicles/<int:pk>/details',FuelSupplyListView.as_view(),name='flota_vehiculos_detalle'),
            path('vehicles/assignment',VehicleAssigmmentListView.as_view(),name='flota_asignacion'),
            path('vehicles/<int:pk>/assignment',VehicleAssignmentView.as_view(),name='flota_vehiculos_asignacion'),
            path('vehicles/<int:pk>/details',VehicleDetailView.as_view(),name='flota_vehiculos_detalle')
            ]



