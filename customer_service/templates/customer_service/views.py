from rest_framework import generics
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestListCreate(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

class ServiceRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
