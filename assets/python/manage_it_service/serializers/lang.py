
from rest_framework import serializers

class setIdiomSerializer(serializers.Serializer):
    idiom = serializers.CharField(max_length = 12)

class updateIdiomSerializer(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
    idiom = serializers.CharField(max_length = 12)

class datIdiomSerializer(serializers.Serializer):
    dat = serializers.CharField(max_length = 20)
