from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import SkillSerializer, SkillCreateSerializer
from capstoneapi.models import Skills, Employer


class Skills(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single skill
        Returns:
            Response -- JSON serialized game type"""
        try:
            skill = Skills.objects.get(pk=pk)
            serializer = SkillSerializer(skill)
            return Response(serializer.data)
        except Skills.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all skills
        Returns:
            Response -- JSON serialized list of game types"""
        skills = Skills.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to skills"""
        user = Employer.objects.get(user=request.auth.user)
        serializer = SkillCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(employer=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Skill"""
        try:
            skill = Skills.objects.get(pk=pk)
            serializer = SkillCreateSerializer(skill, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Skills.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Skill"""
        skill = Skills.objects.get(pk=pk)
        skill.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

