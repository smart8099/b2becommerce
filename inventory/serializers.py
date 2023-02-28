from rest_framework import serializers
from .models import Product, Order
from account.models import CompanyProfile

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


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=CompanyProfile.objects.all(), required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        print('calling this method from serializer')
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        total_amount = 0
        for product in products:
            total_amount += product.price
        order.total_amount = total_amount
        order.save()


        return order

