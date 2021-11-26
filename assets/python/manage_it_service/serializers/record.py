from rest_framework import serializers


class setRecord(serializers.Serializer):
    id_pr = serializers.CharField(max_length = 12)
    monto = serializers.CharField(max_length = 12)
    usuario_creacion = serializers.CharField(max_length = 12)
  
class idRecord(serializers.Serializer):
    id = serializers.CharField(max_length = 8)