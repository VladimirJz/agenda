from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# Catalogs
ADDRESS_TYPE=[(1,'Billable'),(2,'Shipping')]


class Customer(models.Model):
    Name=models.CharField(max_length=30,verbose_name='Nombre',help_text='Nombre del Cliente')
    LastName=models.CharField(max_length=30,verbose_name='Apellidos',help_text='Apellidos')
    DisplayName=models.CharField(max_length=30,verbose_name='Alias',help_text='Nombre alternativo')

class Adress(models.Model):
    AdressType=models.SmallIntegerField(choices=ADDRESS_TYPE,verbose_name='Tipo',help_text='Tipo de dirección')
    Customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    FullAdress=models.CharField(max_length=300,verbose_name='Direccion Completa',help_text='Ingrese la direccion completa')



# class Product(models.Model):
#     Name=
#     SKU=
#     Model=
#     Unity=
#     Size=
#     Peso=
#     Category=
#     SubCategory=
#     Status=
#     Colors=

# class SaleLocations(models.Model):
#     SaleLocationName=



# class Distribution:
#     Product
#     Location

 


