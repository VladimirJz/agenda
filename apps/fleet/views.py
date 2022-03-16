from asyncio import events
from dataclasses import fields
from pipes import Template
from sys import prefix
from typing import Literal
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F
from itertools import chain
from django.db.models import Count
from django.contrib import messages
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy


from apps.fleet import models

from apps.utils import Widgets
from apps.fleet.forms import EventForm,FuelSupplyForm,AssignmentForm
from apps.fleet.models import Assignment, FuelSupply, Vehicle,VehicleClasification,FuelConsumption,Event,State

class dashboard(ListView):
    pass

class VehicleListView(ListView):
    model=Vehicle
    queryset=Vehicle.objects.all().values(  ID=F("id"), 
                                            Marca=F("Manufacturer__ManufacturerName"),
                                            Modelo=F("Model"),
                                            Año=F('Year'),
                                            Color_=F('Color'),
                                            Alias=F('FriendlyName'),
                                            Placas=F('VehiclePlate'),
     
                                        )
                                  
    context_object_name='vehicle_list'

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
       
        #resume.append(Vehicle.objects.filter(Status=1).count()
        # Add in 
        app='flota'
        menu='vehiculos'
        #current_url = self.request.resolver_match.url_name
        breadcrumb=Widgets.Breadcrumb(self)
        context['breadcrumb']=breadcrumb

        #breadcrumb=get_breadcrumb(current_url)

        #TODO: get options from Queryset : Model=> Config.vehicle_options
        options=[
                {'url':'flota_vehiculos_combustible','icon':'fa fa-gas-pump fa-lg','label':'Combustible'},
                {'url':'flota_vehiculos_combustible','icon':'fas fa-wrench','label':'Mantenimiento'},
                {'url':'flota_vehiculos_combustible','icon':'fas fa-car-crash','label':'Incidente'},
                {'url':'flota_vehiculos_combustible','icon':'fas fa-exclamation','label':'Reporte'},

                ]

        context ['menu']=menu
        context['app']=app
        context['options']=options
        context['resume']=resume
        return context

class VehicleAssigmmentListView(ListView):
    model=Vehicle
    #templatename='vehicles/vehicle_assignment_list.html'
    queryset=Vehicle.objects.all().values(ID=F('id'),
                                        Marca=F('Manufacturer__Brand'),
                                        Modelo=F('Model'),
                                        Alias=F('FriendlyName'),
                                        Conductor=F("state__Driver__Employ__DisplayName"),
                                        Placas=F('VehiclePlate'),)
                                        
                                  
    context_object_name='vehicle_list'

    def get_template_names (self):
        return ["fleet/vehicle_assignment_list.html"]
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options=[
                {'url':'flota_vehiculos_asignacion','icon':'fas fa-key','label':'Reasignar'},
                {'url':'flota_vehiculos_asignacion','icon':'fas fa-user-alt-slash','label':'Liberar'},

                ]
        breadcrumb=Widgets.Breadcrumb(self)
        context['breadcrumb']=breadcrumb
        menu='assignment'
        app='fleet'
        context ['menu']=menu
        context['app']=app
        context['options']=options
        return context


class FuelSupplyCreateView(TemplateView,SuccessMessageMixin):
    FUEL_SUPPLY_TYPE=2
    #event_form_class=EventForm
    #fuesupply_form_class=FuelSupplyForm
    template_name='fleet/fuelsupply_create.html'
    #model=Event
    vehicle=Vehicle
    fuel_supply=FuelSupply

    # def get_success_url(self):
    #     return reverse('flota_vehiculos')

    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        self.vehicle=Vehicle.objects.get(id=self.kwargs['pk'])
        context["vehicle"]=self.vehicle
        app='flota'
        menu='combustible'
        go_back='flota_vehiculos'
        breadcrumb=Widgets.Breadcrumb(self)
        context['breadcrumb']=breadcrumb
        context['go_back']=go_back
        context['app']=app
        context['menu']=menu
        return context
        
    def get(self, request, *args, **kwargs):        
        return self.post(request, *args, **kwargs)

    def post(self, request,pk):
        post_data = request.POST or None
        #event_form = self.event_form_class(post_data, prefix='event')
        #fuelsupply_form = self.fuesupply_form_class(post_data, prefix='fuelsupply')
        current_driver=State.objects.filter(Vehicle_id=self.kwargs['pk']).values_list('Driver_id',flat=True)
        event_form = EventForm(post_data, prefix='event',initial={'Driver':current_driver})
        fuelsupply_form = FuelSupplyForm(post_data, prefix='fuelsupply')

        context = self.get_context_data(event_form=event_form,
                                        fuelsupply_form=fuelsupply_form,
                                        )

        if event_form.is_valid():
            if fuelsupply_form.is_valid():
                #self.form_save(event_form)
                event=event_form.save(commit=False)
                fuelsupply=fuelsupply_form.save(commit=False)
                previous_supply=FuelSupply.objects.filter(Event__Vehicle=self.vehicle).order_by('-Event__Date','id').values_list("id","TraveledReading")[:1]
                if(previous_supply):
                    previous_reading=previous_supply[0][1]
                else:
                    previous_reading=0.0
                    
                if(fuelsupply.TraveledReading<previous_reading):
                    messages.add_message(request, messages.WARNING,f'La lectura de kilometraje no es correcta.')
                    messages.add_message(request, messages.INFO,f'La ultima lectura fue de : {(previous_reading):,} ')
                else:
                    event.Vehicle= self.vehicle
                    event.Type=self.FUEL_SUPPLY_TYPE
                    event.update_by=self.request.user
                    event.save()
                    fuelsupply.Event=event
                    fuelsupply.save()
                    
                    consumption=FuelConsumption()
                    consumption.FuelSupply=fuelsupply
                    consumption.FuelQuantity=fuelsupply.Quantity
                    consumption.Driver=event.Driver
                    consumption.StartDate=event.Date
                    consumption.InitialTraveledReading=fuelsupply.TraveledReading
                    consumption.update_by=self.request.user
                    consumption.save()
                    #update the last consumption record
                    last_record=FuelConsumption.objects.filter(FuelSupply__Event__Vehicle=self.vehicle).order_by('-StartDate','id').values_list('id',flat=True)[:1]
                    #last_record=FuelConsumption.objects.filter(FuelSupply__Event__Vehicle=self.vehicle).order_by('-StartDate','id').values_list('id',flat=True)[:1]



                    if(last_record):

                        FuelConsumption.objects.filter(id=last_record).update(EndDate=event.Date,FinalTraveledReading=fuelsupply.TraveledReading)


                    #                 
                    messages.add_message(request, messages.SUCCESS,"Se ha registrado el suministro de combustible")
        return self.render_to_response(context)    


    # def form_save(self, form):
    #     obj = form.save()
    #     messages.success(self.request, "{} saved successfully".format(obj))
    #     return obj



         
class VehicleAssignmentView(TemplateView):
    template_name='fleet/assignment_create.html'
    vehicle=Vehicle
    assignment=Assignment
    ASSIGNMENT_TYPE=7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.vehicle=Vehicle.objects.get(id=self.kwargs['pk'])
        context['vehicle']=self.vehicle
        app='flota'
        menu='asignación'
        go_back='flota_asignacion'
        breadcrumb=Widgets.Breadcrumb(self)
        context['breadcrumb']=breadcrumb
        context['go_back']=go_back
        context['app']=app
        context['menu']=menu
        return context


    def get(self, request, *args, **kwargs):        
        return self.post(request, *args, **kwargs)
    
    def post(self, request,pk):
        post_data = request.POST or None
        current_driver=State.objects.filter(Vehicle_id=self.kwargs['pk']).values_list('Driver_id',flat=True)
        event_form=EventForm(post_data,prefix='event',initial={'Driver':current_driver})
        assignment_form=AssignmentForm(post_data,prefix='assignment')
        context=self.get_context_data(event_form=event_form,
                                        assignment_form=assignment_form
                                        )
        print('post')
        if(post_data):
            if event_form.is_valid():
                print('es valido')
                if assignment_form.is_valid():
                    event=event_form.save(commit=False)
                    assignment=assignment_form.save(commit=False)
                    if(self.is_valid()):
                        print('Ok, validado')
                        event.Vehicle=self.vehicle
                        event.Type=self.ASSIGNMENT_TYPE
                        event.update_by= self.request.user
                        event.save()
                        assignment.Event=event
                        assignment.save()
                        vehicle_state=State.objects.filter(Vehicle=self.vehicle)
                        if(vehicle_state):
                            vehicle_state.update(Driver=assignment.Driver)
                        else:
                            vehicle_state=State.objects.create(Vehicle=self.vehicle,Driver=assignment.Driver,update_by=self.request.user)

                        messages.add_message(request, messages.SUCCESS,"Se ha registrado la asiganación de conductor")
                    else:
                        print('No validado')
                        messages.add_message(request, messages.SUCCESS,"Error general")
                else:
                    print('2 no validado')
            else:   
                raise ValidationError("Ocurrio un error. Intente nuevamente.")

        return self.render_to_response(context)
    
    def is_valid(self):
        return True

class FuelSupplyListView(ListView):
    model=FuelSupply
    queryset= FuelSupply.objects.filter(Event__Vehicle=1).values(Fecha=F("Event__Date"),
                                                                Kilometraje=F("TraveledReading"),
                                                                Cantidad=F("Quantity"),
                                                                Comentarios=F("Comments"),
                                                        )
                                  
    context_object_name='objects'

class VehicleDetailView(DetailView):
    model=Vehicle
    queryset=Vehicle.objects.filter(id=1)
    context_object_name='vehicle'

    def get_template_names (self):
        return ["fleet/vehicle_detail.html"]
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events=(Event.objects.filter(Vehicle_id=1).only('id','Type','Date').order_by('-Date')[:5])
        print (events)
        timeline=[]
        for e in events:
            item={}
            item['id']=e.id
            item['date']=e.Date
            item['icon']=e.icon
            item['level']=e.level
            item['type']=e.get_Type_display()
            timeline.append(item)
            print(item)
        print("---")
        print(timeline)  
        context['events']=timeline
        breadcrumb=Widgets.Breadcrumb(self)
        context['breadcrumb']=breadcrumb
        menu='vehicle'
        app='fleet'
        context ['menu']=menu
        context['app']=app
        return context


class VehicleCreateView(CreateView):
    model=Vehicle
    fields='__all__'
    success_url = reverse_lazy('flota_vehiculos')
    pass