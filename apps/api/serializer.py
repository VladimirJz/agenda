
from rest_framework import serializers

class DummyEmployListSerializer(serializers.Serializer):
    NumEmpleado=serializers.IntegerField(source='employ_id');
    NombreCompleto=serializers.CharField(source='fullname')
    Plaza=serializers.CharField(source='assignment_id')
    Ingreso=serializers.DecimalField(max_digits=9,decimal_places=2,source='salary')
    Puesto=serializers.CharField(source='title')
    Nomina=serializers.CharField(source='company_id');

