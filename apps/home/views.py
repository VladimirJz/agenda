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

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

class EmploySearchView(TemplateView):  
    template_name='home/employ_search.html'
    #context_object_name='search'
    
    # def get(self, request, *args, **kwargs):  

    #     return self.post(request, *args, **kwargs)
    
    def post(self, request):
        post_data = request.POST or None
        print(post_data)
        print(post_data["text_to_search"])
        context=self.get_context_data(text=post_data["text_to_search"])
        return self.render_to_response(context)
    #model=Appointment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options=[{'url':'employ_search','icon':'far fa-calendar-plus','label':'Cita'},
       ]
        print(kwargs)
        text=''
        if( kwargs ):
            text=kwargs['text']
            r= requests.get(f"http://10.186.2.27:8000/apiv1/employ/?name={text}")
            print(r.json())
            context["results"]=r.json()
        else:
            context["results"]={}
        menu='combustible'
        context['app']='employes'
        context['menu']=menu
        context['options']=options
        context['text_to_search']=text
        return context

     