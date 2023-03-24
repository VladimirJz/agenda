# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.appointments.views import AppointmentView
urlpatterns = [
    path('new/', AppointmentView.as_view(), name="appointment_new"),

]
