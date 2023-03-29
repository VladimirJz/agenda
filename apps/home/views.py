# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.appointments.models import Appointment
import requests


class DashboardView(TemplateView):
     template_name='home/index.html'
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        next_events=Appointment.objects.all()
        print(next_events)
        menu='dashboard'
        context['app']='home'
        context['menu']=menu
        context['events']=next_events

        return context

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

class EmploySearchView(TemplateView):  
    template_name='home/employ_search.html'
    
    def post(self, request):
        post_data = request.POST or None
        print(post_data)
        #print(post_data["text_to_search"])
        context=self.get_context_data(text=post_data["text_to_search"])
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options=[{'url':'appointment_new','icon':'far fa-calendar-plus','label':'Cita'},
       ]
        print(kwargs)
        text=''
        if( kwargs ):
            text=kwargs['text']
            if len(text.strip().split(' '))>1:
                try:
                    r= requests.get(f"http://10.186.2.27:8000/apiv1/employ/?name={text}")
                    print(r.json())
                    context["results"]=r.json()
                except :
                    context["results"]=[{"employ_id": 127738,"last_name": "VICENTE MEDINA","names": "NEREIDA","RFC": "VIMN800426B92","CURP": "VIMN800426MOCCDR02","company_id": "2","company": "BASICA","positions": {"job_position_id": 218673,"job_position": "072006A01806000200525","work_place": "20DES0077S","income": "6726.00"}},{"employ_id": 127739,"last_name": "VICENTE MEDINA","names": "NORMA","RFC": "VIMN7705258A4","CURP": "VIMN770525MOCCDR03","company_id": "2","company": "BASICA","positions": {"job_position_id": 69091,"job_position": "078713 E0363120000404","work_place": "20DES0161Q","income": "4805.00"}},{"employ_id": 127739,"last_name": "VICENTE MEDINA","names": "NORMA","RFC": "VIMN7705258A4","CURP": "VIMN770525MOCCDR03","company_id": "2","company": "BASICA","positions": {"job_position_id": 65290,"job_position": "078713 E0363030201608","work_place": "20DES0161Q","income": "1202.00"}},{"employ_id": 127739,"last_name": "VICENTE MEDINA","names": "NORMA","RFC": "VIMN7705258A4","CURP": "VIMN770525MOCCDR03","company_id": "2","company": "BASICA","positions": {"job_position_id": 64003,"job_position": "078713 E0363020201575","work_place": "20DES0161Q","income": "801.00"}},{"employ_id": 127739,"last_name": "VICENTE MEDINA","names": "NORMA","RFC": "VIMN7705258A4","CURP": "VIMN770525MOCCDR03","company_id": "2","company": "BASICA","positions": {"job_position_id": 62009,"job_position": "078713 E0363010100042","work_place": "20DES0161Q","income": "400.00"}},{"employ_id": 127739,"last_name": "VICENTE MEDINA","names": "NORMA","RFC": "VIMN7705258A4","CURP": "VIMN770525MOCCDR03","company_id": "2","company": "BASICA","positions": {"job_position_id": 65484,"job_position": "078713 E0363030201827","work_place": "20DES0161Q","income": "1202.00"}},{"employ_id": 127739,"last_name": "VICENTE MEDINA","names": "NORMA","RFC": "VIMN7705258A4","CURP": "VIMN770525MOCCDR03","company_id": "2","company": "BASICA","positions": {"job_position_id": 62389,"job_position": "078713 E0363010200656","work_place": "20DES0161Q","income": "400.00"}}]
                
        else:
            context["results"]={}
        menu='combustible'
        context['app']='employes'
        context['menu']=menu
        context['options']=options
        context['text_to_search']=text
        return context

     