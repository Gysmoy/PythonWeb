from rest_framework import serializers

class setService(serializers.Serializer):
    service = serializers.CharField(max_length = 45)

class idService(serializers.Serializer):
    id = serializers.CharField(max_length = 8)

class updateService(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
    service = serializers.CharField(max_length = 45)