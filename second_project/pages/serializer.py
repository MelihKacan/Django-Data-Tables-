from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    job = serializers.CharField()