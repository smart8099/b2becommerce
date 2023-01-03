# Generated by Django 4.1.4 on 2022-12-22 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                (
                    "industry_type",
                    models.CharField(
                        choices=[
                            ("MAN", "Manufacturing"),
                            ("CON", "Construction"),
                            ("IT", "Information Technology"),
                            ("PS", "Professional Services"),
                            ("HC", "Healthcare"),
                            ("FS", "Financial Services"),
                            ("WD", "Wholesale and Distribution"),
                            ("RET", "Retail"),
                            ("EDU", "Education"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "tax_identification_number",
                    models.CharField(max_length=15, unique=True),
                ),
                ("address_one", models.CharField(max_length=255)),
                (
                    "address_two",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("phone", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
