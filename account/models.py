from django.db import models
from django.contrib.auth.models import User


class CompanyProfile(models.Model):
    class IndustryType(models.TextChoices):
        MANUFACTURING = "MAN", "Manufacturing"
        CONSTRUCTION = "CON", "Construction"
        IT = "IT", "Information Technology"
        PROFESSIONAL_SERVICES = "PS", "Professional Services"
        HEALTHCARE = "HC", "Healthcare"
        FINANCIAL_SERVICES = "FS", "Financial Services"
        WHOLESALE_AND_DISTRIBUTION = "WD", "Wholesale and Distribution"
        RETAIL = "RET", "Retail"
        EDUCATION = "EDU", "Education"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry_type = models.CharField(max_length=255, choices=IndustryType.choices)
    tax_identification_number = models.CharField(max_length=15, unique=True)
    address_one = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.company_name
