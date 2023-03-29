from django.shortcuts import render

from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,DetailView,ListView
from apps.appointments.models import Appointment
from .forms import AppointmentForm
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
    
        print(self.request.POST)
        return { 'employ_id': self.request.GET.get('id',0) }
    def form_valid(self, form):
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
        return context