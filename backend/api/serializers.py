from rest_framework import serializers
from .models import User, Job, Application

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_employer']

class JobSerializer(serializers.ModelSerializer):
    employer = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = '__all__'
