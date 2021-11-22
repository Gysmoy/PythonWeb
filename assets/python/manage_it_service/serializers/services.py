from rest_framework import serializers

# Serializador de SERVICES
class allService(serializers.Serializer):
    dat = serializers.CharField(max_length = 45)

# Actualizar services serializer
class updateService(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
    service = serializers.CharField(max_length = 45)
    status = serializers.ChoiceField(choices= (('1','Activo'),('0', 'Inactivo')))