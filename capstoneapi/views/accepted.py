from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import AcceptedSerializer, AcceptedCreateSerializer
from capstoneapi.models import Accepted, UserType


class AcceptedView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single accepted
        Returns:
            Response -- JSON serialized game type"""
        try:
            accepted = Accepted.objects.get(pk=pk)
            serializer = AcceptedSerializer(accepted)
            return Response(serializer.data)
        except Accepted.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all accepted
        Returns:
            Response -- JSON serialized list of game types"""
        accepted = Accepted.objects.all()
        serializer = AcceptedSerializer(accepted, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to accepted"""
        serializer = AcceptedCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update accepted"""
        try:
            accepted = Accepted.objects.get(pk=pk)
            serializer = AcceptedCreateSerializer(accepted, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Accepted.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete accepted"""
        accepted = Accepted.objects.get(pk=pk)
        accepted.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)