from rest_framework import serializers
from capstoneapi.models import UserType


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ('__all__')
        depth = 2

class ApplicantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['name', 'user', 'isEmployer']