from django.db import models
from account.models import CompanyProfile
import uuid

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_owner = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='orders')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def calculate_total_amount(self):
        total = 0
        for product in self.products.all():
            total += product.price
        self.total_amount = total
        self.save()


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_address')
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'Shipping address for order {self.order.id}'


