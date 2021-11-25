
from rest_framework import serializers

class queryAdmin(serializers.Serializer):
    query = serializers.CharField(style={'base_template': 'textarea.html'}, max_length = 999999)
