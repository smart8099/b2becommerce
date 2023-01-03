import pytest
from django.contrib.auth.models import User
from account.models import CompanyProfile


@pytest.mark.django_db
def test_company_profile_model():
    # Create a user
    user = User.objects.create_user(
        username="testuser", password="testpass", email="test@example.com"
    )

    # Create a company profile for the user
    company_profile = CompanyProfile.objects.create(
        user=user,
        company_name="Test Company",
        industry_type=CompanyProfile.IndustryType.IT,
        tax_identification_number="123456",
        address_one="123 Main St",
        phone="555-555-5555",
        email="company@example.com",
    )

    # Check that the company profile was created correctly
    assert company_profile.company_name == "Test Company"
    assert company_profile.industry_type == CompanyProfile.IndustryType.IT
    assert company_profile.tax_identification_number == "123456"
    assert company_profile.address_one == "123 Main St"
    assert company_profile.phone == "555-555-5555"
    assert company_profile.email == "company@example.com"
