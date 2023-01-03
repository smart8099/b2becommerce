from rest_framework import generics
from .serializer import CompanyProfileSerializer
from django.contrib.auth.models import User


class CreateCompanyView(generics.CreateAPIView):
    serializer_class = CompanyProfileSerializer

    def perform_create(self, serializer):
        request_data = self.request.data
        serializer.save()
