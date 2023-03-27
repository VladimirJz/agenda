# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home.views import EmploySearchView,DashboardView


urlpatterns = [

    # The home page
    #path('', views.index, name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
    path('', DashboardView.as_view() ,name='home'),
    path('search/',EmploySearchView.as_view(), name='employ_search')
    #path('search/',views.EmploySearchView.as_view(), name='employ_search')
    #re_path('home/'r'^.*\.*', views.pages, name='pages'),
]
