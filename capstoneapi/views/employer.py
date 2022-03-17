from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import EmployerSerializer, EmployerCreateSerializer
from capstoneapi.models import Employer


class EmployerView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single employer
        Returns:
            Response -- JSON serialized game type"""
        try:
            employer = Employer.objects.get(pk=pk)
            serializer = EmployerSerializer(employer)
            return Response(serializer.data)
        except Employer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all employers
        Returns:
            Response -- JSON serialized list of game types"""
        employers = Employer.objects.all()
        serializer = EmployerSerializer(employers, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Update Employer"""
        try:
            employer = Employer.objects.get(pk=pk)
            serializer = EmployerCreateSerializer(employer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Employer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Employer"""
        employer = Employer.objects.get(pk=pk)
        employer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)