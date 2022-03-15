from rest_framework import serializers
from capstoneapi.models import Applied


class AppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applied
        fields = ('__all__')
        depth = 1

class AppliedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applied
        fields = ['posting', 'applicant', 'isAccepted', 'isRejected']