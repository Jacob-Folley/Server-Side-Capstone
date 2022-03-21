from rest_framework import serializers
from capstoneapi.models import Accepted


class AcceptedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accepted
        fields = ('__all__')
        depth = 1

class AcceptedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accepted
        fields = ['posting', 'applicant']