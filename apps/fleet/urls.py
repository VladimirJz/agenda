from django.contrib import admin
from django.urls import path
from apps.fleet.views import EventCreateView, index



urlpatterns=[
            path('vehicle/',index.as_view(),name='index'),
            path('events/new/',EventCreateView.as_view(),name='event_new'),#servernew

            ]



