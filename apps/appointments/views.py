from django.shortcuts import render
from django.views.generic import TemplateView
from apps.appointments.models import Schedule,Appointment

# Create your views here.

class AppointmentView(TemplateView):  
    model=Appointment
    template_name='appointments/appointment_create.html'

    