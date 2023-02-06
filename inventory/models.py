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

