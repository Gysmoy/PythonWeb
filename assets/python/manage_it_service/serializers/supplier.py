from rest_framework import serializers

class idUser(serializers.Serializer):
    id = serializers.CharField(max_length = 8)


    