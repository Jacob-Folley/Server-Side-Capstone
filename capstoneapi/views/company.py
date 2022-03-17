from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import CompanySerializer, CompanyCreateSerializer
from capstoneapi.models import Company, Employer


class CompanyView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single company
        Returns:
            Response -- JSON serialized game type"""
        try:
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    # NEED TO ADD A FILTER TO THIS SO ONLY CAN GET A LIST OF RESUMES POSTED BY THAT APPLICANT
    # def list(self, request):
    #     """Handle GET requests to get all resumes
    #     Returns:
    #         Response -- JSON serialized list of game types"""
    #     skills = Skills.objects.all()
    #     serializer = SkillSerializer(skills, many=True)
    #     return Response(serializer.data)

    def create(self, request):
        """Handle post requests to company"""
        user = request.auth.user
        serializer = CompanyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(employer=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Company"""
        try:
            company = Company.objects.get(pk=pk)
            serializer = CompanyCreateSerializer(company, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Company.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Company"""
        company = Company.objects.get(pk=pk)
        company.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)