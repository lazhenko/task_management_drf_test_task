from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'created_at', 'updated_at', 'user']
        read_only_fields = ['created_at', 'updated_at', 'user']
