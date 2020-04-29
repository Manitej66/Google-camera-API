from rest_framework import serializers
from .models import Gcam


class GcamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gcam
        fields = '__all__'
