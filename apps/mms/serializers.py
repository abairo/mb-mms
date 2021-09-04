from .models import MMS
from rest_framework import serializers


class MMSSerializer(serializers.ModelSerializer):
    mms = serializers.FloatField()

    class Meta:
        model = MMS
        fields = ('timestamp', 'mms')
