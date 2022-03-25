from rest_framework import serializers
from capstoneapi.models import Job_Posting


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posting
        fields = ('id', 'employer', 'title', 'description', 'skills', 'applications', 'company')
        depth = 2

class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posting
        fields = ['title', 'description', 'skills', 'company']