from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer

class WorkerListCreate(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

