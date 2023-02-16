from rest_framework import serializers
from main.models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'