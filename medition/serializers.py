from rest_framework import serializers
from medition.models import Meditions

class MeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditions
        fields = ('MeditionId', 'Ph', 'Voltage', 'Current')