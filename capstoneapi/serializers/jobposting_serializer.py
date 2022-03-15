from rest_framework import serializers
from capstoneapi.models import Job_Posting


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posting
        fields = ('__all__')
        depth = 1

class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posting
        fields = ['employer', 'description', 'skills']