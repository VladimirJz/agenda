# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from apps.company.models import UserProfile
import requests


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(user)
                print(user.id)
                profile=UserProfile.objects.filter(User_id=user.id).select_related()
                for p in profile:
                    print(p)
                    print(type(p))
                    secret=p.APISecret
                    print(secret)
                    user_name=p.User.username
                    secret=p.APISecret
                data =dict()
                data['username']=user_name
                data['password']=secret
                r=requests.post('http://api.ieepo.gob.mx:8000/apiv1/auth/login/',data=data)
                response=r.json()
                token=response['token'] 
                print(token)
                session = UserProfile.objects.filter(User_id=user.id)[0]
                session.Token=token
                session.save()

                #user_name=profile[0]['User__username']
                #secret=profile[0]['APISecret']

                print(secret)
                print(user_name)
                return redirect("/home/")
            else:
                msg = 'Credenciales no valida'
        else:
            msg = 'Error al validar las credenciales'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
