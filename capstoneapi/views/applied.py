from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import AppliedSerializer, AppliedCreateSerializer
from capstoneapi.models import Applied, UserType


class AppliedView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single applied
        Returns:
            Response -- JSON serialized game type"""
        try:
            applied = Applied.objects.get(pk=pk)
            serializer = AppliedSerializer(applied)
            return Response(serializer.data)
        except Applied.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all applied
        Returns:
            Response -- JSON serialized list of game types"""
        applied = Applied.objects.all()
        serializer = AppliedSerializer(applied, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to applied"""
        user = UserType.objects.get(user=request.auth.user)
        serializer = AppliedCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(applicant=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Applied"""
        try:
            applied = Applied.objects.get(pk=pk)
            serializer = AppliedCreateSerializer(applied, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Applied.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Applied"""
        applied = Applied.objects.get(pk=pk)
        applied.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)