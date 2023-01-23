from rest_framework import serializers
from .models import *

class RotiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotiModel
        fields = '__all__'