
from rest_framework import serializers
# crear nueba persona natural

class setP_naturalSerializer(serializers.Serializer):
    apePater = serializers.CharField(max_length = 15)
    apeMater = serializers.CharField(max_length = 15)
    nombres = serializers.CharField(max_length = 45)
    dni = serializers.CharField(max_length = 8)
    id_servicio = serializers.CharField(max_length = 8)
    tel1 = serializers.CharField(max_length = 15)
    tel2 = serializers.CharField(max_length = 15)
    correo = serializers.CharField(max_length = 320)
    direccion = serializers.CharField(max_length = 250)
    # multi usos

class allUseSerializer(serializers.Serializer):
    dat = serializers.CharField(max_length = 30)
# actualizar persona natural

class updateP_naturalSerializer(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
    apePater = serializers.CharField(max_length = 15)
    apeMater = serializers.CharField(max_length = 15)
    nombres = serializers.CharField(max_length = 45)
    dni = serializers.CharField(max_length = 8)
    id_servicio = serializers.CharField(max_length = 8)
    tel1 = serializers.CharField(max_length = 15)
    tel2 = serializers.CharField(max_length = 15)
    correo = serializers.CharField(max_length = 320)
    direccion = serializers.CharField(max_length = 250)
    estado = serializers.ChoiceField(choices = (('1', 'ACTIVO'), ('0', 'INACTIVO')))