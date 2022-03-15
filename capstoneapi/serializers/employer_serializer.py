from rest_framework import serializers
from capstoneapi.models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('__all__')
        depth = 1

class EmployerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['company', 'user']