from rest_framework import serializers
from capstoneapi.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('__all__')
        depth = 1

class ResumeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['applicant', 'resume', 'skills']