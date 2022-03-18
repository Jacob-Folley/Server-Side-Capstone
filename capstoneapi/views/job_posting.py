from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from capstoneapi.serializers import JobPostingSerializer, JobPostingCreateSerializer
from capstoneapi.models import Job_Posting


class Job_PostingView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single job posting
        Returns:
            Response -- JSON serialized game type"""
        try:
            job_posting = Job_Posting.objects.get(pk=pk)
            serializer = JobPostingSerializer(job_posting)
            return Response(serializer.data)
        except Job_Posting.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all job postings
        Returns:
            Response -- JSON serialized list of game types"""
        job_postings = Job_Posting.objects.all()
        serializer = JobPostingSerializer(job_postings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to job posting"""
        user = request.auth.user
        serializer = JobPostingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(employer=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Job Posting"""
        try:
            job_posting = Job_Posting.objects.get(pk=pk)
            serializer = JobPostingCreateSerializer(job_posting, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Job_Posting.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Job Posting"""
        job_posting = Job_Posting.objects.get(pk=pk)
        job_posting.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)