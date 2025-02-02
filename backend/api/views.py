from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Job
from .serializers import *


class JobView(APIView):
    permission_classes  = [permissions.IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.all
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)