from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework.renderers import BrowsableAPIRenderer

from inventory.models import Product
from account.models import CompanyProfile
from rest_framework.exceptions import NotFound

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from .serializers import ProductSerializer
from .permissions import IsProductOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProductViewSet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        user_id = self.request.user.id
        print(f"the logged in user id is {user_id}")
        real_id = CompanyProfile.objects.get(user_id=user_id).id
        print(f"the company profile id of the logged in user is {real_id}")
        serializer.save(product_owner_id=real_id)

class ProductsList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,IsProductOwnerOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'

    def get_object(self):

        try:
            pk = self.kwargs.get("uuid")
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound(detail="The requested resource was not found")

class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,IsProductOwnerOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get("uuid")
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound(detail="The requested resource was not found")

    def perform_destroy(self, instance):
        instance.delete()

class ProductUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,IsProductOwnerOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get("uuid")
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound(detail="The requested resource was not found")

    def perform_update(self, serializer):
        serializer.save()

# class OrderCreateView(generics.CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#     def perform_create(self, serializer):
#         order = serializer.save(total_cost=serializer.calculate_total_cost())
#         return order
