from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import DummyEmployListSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
##

from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

# Create your views here.

class DummyEmployList(APIView):


    def get(self, request, format=None):
        employ_list =[
        {"employ_id":131,"fullname":"Marcos Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Basica","salary":4500.00},
        {"employ_id":244,"fullname":"Miguel Hidalgo I. Costilla","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":355,"fullname":"Agustin Melgar","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Basica","salary":7800.00},
        {"employ_id":534,"fullname":"Fernando Pablo de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Mandos medios","salary":8900.00},
        {"employ_id":141,"fullname":"Antonio Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Mandos medios","salary":4500.00},
        {"employ_id":562,"fullname":"Miguel Lopez I. Neri","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":347,"fullname":"Agustin Melgar","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Mandos medios","salary":7800.00},
        {"employ_id":436,"fullname":"Fernando Montes de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Mandos medios","salary":8900.00},
        {"employ_id":144,"fullname":"Mateo Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Mandos medios","salary":4500.00},
        {"employ_id":254,"fullname":"Miguel Martinez I. Costilla","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":372,"fullname":"Fernando Melgar","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Basica","salary":7800.00},
        {"employ_id":942,"fullname":"Ramiro Montes de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Basica","salary":8900.00},
        {"employ_id":144,"fullname":"Mateo Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Mandos medios","salary":4500.00},
        {"employ_id":254,"fullname":"Miguel Martinez I. Costilla","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":372,"fullname":"Fernando Altamirano","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Basica","salary":7800.00},
        {"employ_id":942,"fullname":"Jesus Montes de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Basica","salary":8900.00},
        ]

    
        serializer = DummyEmployListSerializer(employ_list, many=True)
        return Response(serializer.data)


class DummyExportList(XLSXFileMixin,APIView):
    renderer_classes = [XLSXRenderer,]
    #serializer_class=DummyEmployListSerializer
    filename = 'reporte_empleados.xlsx'

    column_header = {
        
        'column_width': [17, 30, 17,30,30],
        'height': 25,
        'style': {
            'fill': {
                'fill_type': 'solid',
                'start_color': 'FFCCFFCC',
            },
            'alignment': {
                'horizontal': 'center',
                'vertical': 'center',
                'wrapText': True,
                'shrink_to_fit': True,
            },
            'border_side': {
                'border_style': 'thin',
                'color': 'FF000000',
            },
            'font': {
                'name': 'Arial',
                'size': 11,
                'bold': True,
                'color': 'FF000000',
            },
        },
    }
    body = {
        'style': {
                'fill': {
                        'fill_type': 'solid',
                        'start_color': 'FFACFFCC',
                        },
                'alignment': {
                    'horizontal': 'auto',
                    'vertical': 'auto',
                    'wrapText': True,
                    'shrink_to_fit': False,
                    },
            'border_side': {
                'border_style': 'thin',
                'color': 'FF000000',
                },
            'font': {
                'name': 'Arial',
                'size': 11,
                'bold': False,
                'color': 'FF000000',
                }
        },
        'height': 13,
    }  
    
    def get_serializer(self, instance=None, data=None, many=False, partial=False):
        serializer = DummyEmployListSerializer()
        return serializer

    def get(self, request, format=None):

        employ_list =[
        {"employ_id":131,"fullname":"Marcos Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Basica","salary":4500.00},
        {"employ_id":244,"fullname":"Miguel Hidalgo I. Costilla","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":355,"fullname":"Agustin Melgar","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Basica","salary":7800.00},
        {"employ_id":534,"fullname":"Fernando Pablo de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Mandos medios","salary":8900.00},
        {"employ_id":141,"fullname":"Antonio Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Mandos medios","salary":4500.00},
        {"employ_id":562,"fullname":"Miguel Lopez I. Neri","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":347,"fullname":"Agustin Melgar","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Mandos medios","salary":7800.00},
        {"employ_id":436,"fullname":"Fernando Montes de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Mandos medios","salary":8900.00},
        {"employ_id":144,"fullname":"Mateo Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Mandos medios","salary":4500.00},
        {"employ_id":254,"fullname":"Miguel Martinez I. Costilla","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":372,"fullname":"Fernando Melgar","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Basica","salary":7800.00},
        {"employ_id":942,"fullname":"Ramiro Montes de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Basica","salary":8900.00},
        {"employ_id":144,"fullname":"Mateo Lopez de Santa Ana","assignment_id":"1111111","title":"Jefe de Pagos","company_id":"Mandos medios","salary":4500.00},
        {"employ_id":254,"fullname":"Miguel Martinez I. Costilla","assignment_id":"2222222","title":"Asistente","company_id":"Mandos medios","salary":5600.00},
        {"employ_id":372,"fullname":"Fernando Altamirano","assignment_id":"3333333","title":"Coordinador de compras","company_id":"Basica","salary":7800.00},
        {"employ_id":942,"fullname":"Jesus Montes de Oca","assignment_id":"4444444","title":"Jefe de materiales","company_id":"Basica","salary":8900.00},
        ]

    
        serializer = DummyEmployListSerializer(employ_list, many=True)
        print(serializer)
        return Response(serializer.data)

