from rest_framework import serializers
class setSubscriptions(serializers.Serializer):
    id_proveedor = serializers.CharField(max_length = 10)
    id_ciclos = serializers.CharField(max_length = 10)
    id_moneda = serializers.CharField(max_length = 10)
    monto = serializers.CharField(max_length = 10)
    fec_inicio = serializers.CharField(max_length = 10)
    prorroga = serializers.CharField(max_length = 15)
    usuario_creacion = serializers.CharField(max_length = 15)
    
class idSub(serializers.Serializer):
    id = serializers.CharField(max_length = 10)

class updateSubs(serializers.Serializer):
    id = serializers.CharField(max_length = 10)
    id_proveedor = serializers.CharField(max_length = 10)
    id_ciclos = serializers.CharField(max_length = 10)
    id_moneda = serializers.CharField(max_length = 10)
    monto = serializers.CharField(max_length = 10)
    fec_inicio = serializers.CharField(max_length = 10)
    prorroga = serializers.CharField(max_length = 15)