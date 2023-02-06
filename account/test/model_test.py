import pytest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from account.models import CompanyProfile



@pytest.mark.django_db
def test_company_profile_creation():
    User = get_user_model()
    user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )
    company_profile = CompanyProfile.objects.create(
        user=user,
        company_name='Test Company',
        industry_type=CompanyProfile.IndustryType.IT,
        tax_identification_number='1234567890',
        address_one='123 Test Street',
        phone='555-555-5555',
        email='test@example.com'
    )
    assert isinstance(company_profile, CompanyProfile)
    assert str(company_profile) == 'Test Company'

@pytest.mark.django_db
def test_industry_type_choices():
    print(type(CompanyProfile.IndustryType.MANUFACTURING))
    assert CompanyProfile.IndustryType.MANUFACTURING[:] == 'MAN'
    assert CompanyProfile.IndustryType.IT[:] == 'IT'

@pytest.mark.django_db
def test_tax_identification_number_unique():
    User = get_user_model()
    user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )
    CompanyProfile.objects.create(
        user=user,
        company_name='Test Company',
        industry_type=CompanyProfile.IndustryType.IT,
        tax_identification_number='1234567890',
        address_one='123 Test Street',
        phone='555-555-5555',
        email='test@example.com'
    )
    with pytest.raises(IntegrityError) as e:
        duplicate_profile = CompanyProfile(
            user=user,
            company_name='Duplicate Company',
            industry_type=CompanyProfile.IndustryType.IT,
            tax_identification_number='1234567890',
            address_one='456 Test Street',
            phone='555-555-5555',
            email='duplicate@example.com'
        )
        duplicate_profile.save()

@pytest.mark.django_db
def test_email_unique():
    User = get_user_model()
    user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )
    CompanyProfile.objects.create(
        user=user,
        company_name='Test Company',
        industry_type=CompanyProfile.IndustryType.IT,
        tax_identification_number='0987654321',
        address_one='123 Test Street',
        phone='555-555-5555',
        email='test@example.com'
    )
    with pytest.raises(IntegrityError) as e:
        duplicate_profile = CompanyProfile(
            user=user,
            company_name='Duplicate Company',
            industry_type=CompanyProfile.IndustryType.IT,
            tax_identification_number='0123456789',
            phone='555-555-5555',
            email='test@example.com'
        )
        duplicate_profile.save()
