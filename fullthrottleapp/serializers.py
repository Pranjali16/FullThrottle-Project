from rest_framework import serializers
from .models import *


class ActivityPeriodSerializer(serializers.ModelSerializer):
    """Serializer to display activity period"""

    class Meta:
        model = ActivityPeriod
        fields = '__all__'
