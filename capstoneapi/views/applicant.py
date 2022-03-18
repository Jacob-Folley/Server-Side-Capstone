from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import ApplicantSerializer, ApplicantCreateSerializer
from capstoneapi.models import UserType


class ApplicantView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single applicant
        Returns:
            Response -- JSON serialized game type"""
        try:
            applicant = UserType.objects.get(pk=pk)
            serializer = ApplicantSerializer(applicant)
            return Response(serializer.data)
        except UserType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all applicants
        Returns:
            Response -- JSON serialized list of game types"""
        applicant = UserType.objects.all()
        serializer = ApplicantSerializer(applicant, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Update Applicant"""
        try:
            applicant = UserType.objects.get(pk=pk)
            serializer = ApplicantCreateSerializer(applicant, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except UserType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Skill"""
        applicant = UserType.objects.get(pk=pk)
        applicant.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)