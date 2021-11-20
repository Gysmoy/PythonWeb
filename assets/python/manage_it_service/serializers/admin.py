
from rest_framework import serializers

class queryAdmin(serializers.Serializer):
    query = serializers.CharField(max_length = 250)
