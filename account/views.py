from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from account.permissions import IsNotAuthenticated,IsCompanyProfileOwner
from account.models import CompanyProfile
from .serializers import CompanyProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class CreateCompanyProfileView(generics.CreateAPIView):
    permission_classes = (AllowAny,IsNotAuthenticated,)
    serializer_class = CompanyProfileSerializer

    def perform_create(self, serializer):

        request_data = self.request.data
        serializer.save()

class DetailCompanyProfileView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,IsCompanyProfileOwner)
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    lookup_field = 'id'


class UpdateCompanyProfileView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,IsCompanyProfileOwner)
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    lookup_field = 'id'

class DeleteCompanyProfileView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,IsCompanyProfileOwner)
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    lookup_field = 'id'


    def perform_destroy(self, instance):
        logout(self.request) # logs out the user
        instance.delete()

