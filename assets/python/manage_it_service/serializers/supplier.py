from rest_framework import serializers

class setSupplier(serializers.Serializer):
    tipo = serializers.CharField(max_length = 1)
    id_per_nat = serializers.CharField(max_length = 8, min_length=0, allow_blank=True)
    id_per_jur = serializers.CharField(max_length = 8, min_length=0, allow_blank=True)
    usuario_creacion = serializers.CharField(max_length = 10)

class updateSupplier(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
    tipo = serializers.CharField(max_length = 1)
    id_per_nat = serializers.CharField(max_length = 8)
    id_per_jur = serializers.CharField(max_length = 8)

class idUser(serializers.Serializer):
    id_user = serializers.CharField(max_length = 10)

class idSupplier(serializers.Serializer):
    id = serializers.CharField(max_length = 10)

    