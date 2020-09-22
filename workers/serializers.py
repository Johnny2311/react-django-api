from rest_framework import serializers
from .models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['name', 'birthdate', 'address', 'phone', 'email', 'dni', 'deparment']