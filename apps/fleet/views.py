from multiprocessing import Event
from typing import Literal
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.messages.views import SuccessMessageMixin
from apps.fleet.forms import NewEventForm

from apps.fleet.models import Vehicle,VehicleClasification
from django.db.models import F
from itertools import chain
class index(ListView):
    model=Vehicle
    queryset=Vehicle.objects.all().values(  
                                            Marca=F("Manufacturer__ManufacturerName"),
                                            Modelo=F("Model"),
                                            Año=F('Year'),
                                            Color_=F('Color'),
                                            Alias=F('FriendlyName'),
                                            Placas=F('VehiclePlate'),
                      
                     
                     
        

                                        )
                                  
    context_object_name='objects'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in 
        app='catalog'
        menu='tables'
        current_url = self.request.resolver_match.url_name
        #breadcrumb=get_breadcrumb(current_url)
        #context['breadcrumb']=breadcrumb
        options=[{'url':'link_history'},{'ico':'fa fa-calendar-check fa-lg'},{'alt':'Actualizar'},{'url':'link_eliminar'},{'ico':'fa fa-gas-pump fa-lg'},{'alt':'Detalle'}]
        context ['menu']=menu
        context['app']=app
        context['options']=options
        return context
    

class EventCreateView(SuccessMessageMixin,CreateView):
    model = Event
    template_name = 'fleet/event_new.html'
    form_class = NewEventForm
    

# Create your views here.
