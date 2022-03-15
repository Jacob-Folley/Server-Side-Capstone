from rest_framework import serializers
from capstoneapi.models import Skills


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('__all__')
        depth = 1

class SkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['skill']