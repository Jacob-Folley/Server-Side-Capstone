from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import ResumeSerializer, ResumeCreateSerializer, SkillSerializer
from capstoneapi.models import Resume, UserType, Skills
from django.shortcuts import render
# from somewhere import handle_uploaded_file
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import uuid
import base64
from django.core.files.base import ContentFile



class ResumeView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single resume
        Returns:
            Response -- JSON serialized game type"""
        try:
            resume = Resume.objects.get(pk=pk)
            serializer = ResumeSerializer(resume)
            return Response(serializer.data)
        except Resume.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all resumes
        Returns:
            Response -- JSON serialized list of game types"""
        skills = Skills.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to resume"""
        user = request.auth.user
        
        format, imgstr = request.data["resume"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["resume"]}-{uuid.uuid4()}.{ext}')
        serializer = ResumeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(applicant=user, resume=data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Resume"""
        try:
            resume = Resume.objects.get(pk=pk)
            serializer = ResumeCreateSerializer(resume, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Resume.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Resume"""
        resume = Resume.objects.get(pk=pk)
        resume.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)