from rest_framework import viewsets

from services.models import Service
from services.serializers import ServiceSerializer


class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('-created_at')
    serializer_class = ServiceSerializer
