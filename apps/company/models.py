from re import T
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, DecimalField, IntegerField, SmallIntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Profile(models.Model):
    CompanyName=models.CharField(max_length=50,verbose_name='Nombre',help_text='Nombre comercial')
    TaxPayerID=models.CharField(max_length=13,verbose_name='RFC', help_text='RFC',blank=True)
    TradeName=models.CharField(max_length=50,verbose_name='Razón Social',help_text='Razón Social de la empresa')
    Slogan=models.CharField(max_length=50,verbose_name='Eslogan',help_text='Eslogan',default='',blank=True)



class Office(models.Model):
    OfficeName=models.CharField(max_length=100,verbose_name='Office',help_text='Office name')
    def __str__(self):
        return self.OfficeName


class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    BirthDate = models.DateField(null=True, blank=True)

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.UserProfile.save()
    def __str__(self):
        return self.User.first_name


class Employ(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Name=models.CharField(max_length=200,help_text='Name')
    LastName=models.CharField(max_length=200,help_text='LastName',default='',blank=True)
    DisplayName=models.CharField(max_length=200,help_text='Firstname',default='',blank=True,null=True)
    RFC =  CharField(max_length=13,help_text='RFC',blank=True,default='',null=True)
    CURP=  CharField(max_length=18,help_text='CURP',blank=True,default='',null=True)
    JobTittle=models.CharField(max_length=50,help_text='Job tittle',blank=True,null=True)
    CompanyEmail=models.EmailField(_("Office Email"), max_length=200)
    PersonalEmail=models.EmailField(_("Personal Email"), max_length=30,blank=True,null=True)
    PhoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    PhoneNumber=models.CharField(validators = [PhoneNumberRegex], max_length = 16, blank=True, null=True)
    Office=models.ForeignKey(Office,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.Name +' '+ self.LastName
    