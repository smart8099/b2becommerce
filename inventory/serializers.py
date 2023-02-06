from rest_framework import serializers
from .models import Product


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # product_owner = serializers.PrimaryKeyRelatedField()

    class Meta:
        product_owner_id = serializers.IntegerField()
        model = Product
        fields = ["id", "name", "sku", "price", "description", "quantity", "unit"]
        # fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     customer = serializers.PrimaryKeyRelatedField(read_only=True)
#     products = ProductSerializer(many=True)
#
#     class Meta:
#         model = Order
#         fields = [
#             "id",
#             "customer",
#             "products",
#             "quantities",
#             "total_cost",
#             "order_date",
#             "shipping_address",
#             "status",
#         ]
