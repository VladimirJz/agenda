from multiprocessing import Event
from pipes import Template
from typing import Literal
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F
from itertools import chain
from django.db.models import Count
from django.contrib import messages

from apps.utils import Site
from apps.fleet.forms import NewEventForm,EventForm,FuelSupplyForm
from apps.fleet.models import Vehicle,VehicleClasification

class dashboard(ListView):
    pass

class index(ListView):
    model=Vehicle
    queryset=Vehicle.objects.all().values(  ID=F("id"), 
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
        breadcrumb=Site.Breadcrumb(self)
        context['breadcrumb']=breadcrumb

        #breadcrumb=get_breadcrumb(current_url)

        #TODO: get options from Queryset : Model=> Config.vehicle_options
        options=[
                {'url':'fuelsupply/','ico':'fa fa-gas-pump fa-lg','alt':'Combustible'},
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

class FuelSupplyCreateView(TemplateView):
    event_form_class=EventForm
    fuesupply_form_class=FuelSupplyForm
    template_name='fleet/fuelsupply_create.html'

    def post(self, request):
        post_data = request.POST or None
        event_form = self.event_form_class(post_data, prefix='event')
        fuelsupply_form = self.fuesupply_form_class(post_data, prefix='fuelsupply')

        context = self.get_context_data(event_form=event_form,
                                        fuelsupply_form=fuelsupply_form)

        if event_form.is_valid():
            self.form_save(event_form)
        if fuelsupply_form.is_valid():
            self.form_save(fuelsupply_form)

        return self.render_to_response(context)     

    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    pass
    

# Create your views here.
