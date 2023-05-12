from django.shortcuts import render,HttpResponseRedirect,redirect
from datetime import datetime,timedelta
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,DetailView,ListView
from apps.appointments.models import Appointment
from apps.company.models import UserProfile
from .forms import AppointmentForm
import requests
# Create your views here.

class AppointmentView(TemplateView):  
    model=Appointment
    template_name='appointments/appointment_create.html'

class AppoinmentUpdateView (UpdateView):
    model=Appointment 
    form_class=AppointmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['go_back']='home'
        context['app']='appointment'
        return context 

class AppoinmentCreateView(CreateView):
    model=Appointment
    #fields='__all__'
    form_class=AppointmentForm


    def get_initial(self):
        #print(self.request)
    
        #print(self.request.POST)
        empleado_id=self.kwargs['id']
        default={}
        session=UserProfile.objects.filter(User_id=self.request.user.id).values('Token')[0]
        token=session['Token']
        headers={'Authorization':'Token '+ token}
        try:
            r= requests.get(f"http://10.186.11.3:8000/apiv1/employ/{empleado_id}",headers=headers)
            print(r.json())
            result=r.json()
        except :
            result={}

        default['employ_name']=result.get('fullname','')
        default['position']=result.get('title','')
        default['employ_id']=self.kwargs['id']
        default['date']=datetime.now()  +  timedelta(days=1)
        default['priority']=3
        print(default)
        return default
    



    def form_valid(self, form):
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user_id = self.request.user.id
            appointment.save()
            print(appointment.id)
            print(appointment.pk)
            return redirect('appointment_detail',pk=appointment.pk)


        #form.instance.owner = self.request.user

        form.save() # tried this too and it didn't work
        return super().form_valid(form)
    def get_form(self):
        form = super().get_form()
        # form.fields["date"].widget = DatePickerInput()
        # form.fields["start"].widget = TimePickerInput()
        # form.fields["end"].widget = TimePickerInput()
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['go_back']='home'
        context['app']='appointment'
        return context
class AppointmentDetailView(DetailView):
    model=Appointment
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['go_back']='home'
        context['app']='appointment'
        return context
class AppointmentListView(ListView):
    model=Appointment
    context_object_name = 'events'
    queryset = Appointment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['go_back']='home'
        context['app']='appointment'
        options={'icon':'fas fa-tasks','text':'','menu':[{'url':'appointment_detail','icon':'far fa-calendar-plus','label':'Abierta'},{'url':'appointment_detail','icon':'far fa-calendar-plus','label':'Pendiente'},{'url':'appointment_detail','icon':'far fa-calendar-plus','label':'Cancelar'}]}
        context['options']=options

        return context