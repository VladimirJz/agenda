from multiprocessing import Event
from typing import Literal
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.messages.views import SuccessMessageMixin
from apps.fleet.forms import NewEventForm

from apps.fleet.models import Vehicle,VehicleClasification
from django.db.models import F
from itertools import chain
from django.db.models import Count
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
        resume=[]
        vehicles=Vehicle.objects.all()
        all=vehicles.count()
        availables=vehicles.filter(Status=1).count()
        on_road=vehicles.filter(Status=2).count()
        stopped=vehicles.filter(Status=3).count()
        resume=dict(all=all,availables=availables,on_road=on_road,stopped=stopped)


        print(all,availables,on_road,stopped)
        print(resume)
        #resume.append(Vehicle.objects.filter(Status=1).count()
        # Add in 
        app='catalog'
        menu='tables'
        current_url = self.request.resolver_match.url_name
        #breadcrumb=get_breadcrumb(current_url)
        #context['breadcrumb']=breadcrumb

        #TODO: get options from Queryset : Model=> Config.vehicle_options
        options=[
                {'url':'#','ico':'fa fa-gas-pump fa-lg','alt':'Combustible'},
                {'url':'#','ico':'fas fa-wrench','alt':'Mantenimiento'},
                {'url':'#','ico':'fas fa-car-crash','alt':'Incidente'},
                {'url':'#','ico':'fas fa-exclamation','alt':'Reporte'},

                ]

        context ['menu']=menu
        context['app']=app
        context['options']=options
        context['resume']=resume
        return context
    

class EventCreateView(SuccessMessageMixin,CreateView):
    model = Event
    template_name = 'fleet/event_new.html'
    form_class = NewEventForm
    

# Create your views here.
