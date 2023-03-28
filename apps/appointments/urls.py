# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.appointments.views import AppointmentView, AppoinmentCreateView,AppointmentDetailView,AppoinmentUpdateView,AppointmentListView
urlpatterns = [
    path('<int:id>/new/', AppoinmentCreateView.as_view(), name="appointment_new"),
    path('<int:pk>/', AppointmentDetailView.as_view(), name="appointment_detail"),
    path('<int:pk>/update', AppoinmentUpdateView.as_view(), name="appointment_update"),
    path('', AppointmentListView.as_view(), name="appointment_list"),

]
