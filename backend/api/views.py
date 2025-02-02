from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Job, Application, User
from .serializers import JobSerializer, ApplicationSerializer
from django.shortcuts import get_object_or_404

# Job CRUD API
class JobView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.User.is_employer:
            return Response({"error": "Only employers can post jobs"}, status=status.HTTP_403_FORBIDDEN)

        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Apply for a Job
class ApplyJobView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        serializer = ApplicationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(applicant=request.user, job=job)
            return Response({"message": "Application submitted"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
