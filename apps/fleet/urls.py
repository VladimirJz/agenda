from django.contrib import admin
from django.urls import path
from apps.fleet.views import index



urlpatterns=[
            path('vehicle/',index.as_view(),name='index'),

            ]



