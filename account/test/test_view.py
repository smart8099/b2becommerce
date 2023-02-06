
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
import json
from rest_framework import status
from account.permissions import IsCompanyProfileOwner
from account.models import CompanyProfile
from account.views import CreateCompanyProfileView
from account.views import DetailCompanyProfileView
from account.views import UpdateCompanyProfileView
from account.views import DeleteCompanyProfileView
from account.serializers import CompanyProfileSerializer

@pytest.fixture
def create_user(client):
    user = get_user_model().objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    return user

@pytest.fixture
def create_company_profile(create_user):
    company_profile = CompanyProfile.objects.create(
        user=create_user,
        company_name='Test Company',
        industry_type='IT',
        tax_identification_number='1234567890',
        address_one='123 Test Street',
        phone='555-555-5555',
        email='test@example.com'
    )
    return company_profile

@pytest.mark.django_db
def test_create_company_profile(client):

    # create a user to associate with the company
    data = {
        "user":  {
            "username": "testuser21",
            "password1": "testpassword",
            "password2": "testpassword"
        },
        "company_name": "Test Company",
        "industry_type": "IT",
        "tax_identification_number": "1234567890",
        "address_one": "123 Test Street",
        "phone": "555-555-5555",
        "email": "test@example.com"
    }

    response = client.post('/accounts/companies/create/',json.dumps(data),content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['company_name'] == 'Test Company'

@pytest.mark.django_db
def test_detail_company_profile(client, create_user, create_company_profile):
    response = client.get(f'/accounts/companies/{create_company_profile.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['company_name'] == 'Test Company'

# @pytest.mark.django_db
# def test_update_company_profile(client, create_user, create_company_profile):
#
#     data = {'company_name': 'Updated Company'}
#     print(f'the current company name is {create_company_profile.company_name}')
#     response = client.patch(f'/accounts/companies/update/{create_company_profile.id}/', json=data,content_type='application/json')
#     print(response.content)
#     create_company_profile.refresh_from_db()
#
#     print(f'the id of the update is /accounts/companies/update/{create_company_profile.id}/')
#     assert response.status_code == status.HTTP_200_OK
#     assert create_company_profile.company_name == 'Updated Company'

@pytest.mark.django_db
def test_delete_company_profile(client, create_user, create_company_profile):
    response = client.delete(f'/accounts/companies/delete/{create_company_profile.id}/')

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert CompanyProfile.objects.count() == 0

# @pytest.mark.django_db
# @pytest.mark.django_db
# def test_create_company_profile_permission(client):
#     client.logout()
#     response = client.post('/accounts/companies/create/', json.dumps({
#     'user': {
#         'username': 'testuser',
#         'password1': 'testpassword',
#         'password2': 'testpassword'
#     },
#
#     'company_name': 'Test Company',
#     'industry_type': 'IT',
#     'tax_identification_number': '1234567890',
#     'address_one': '123 Test Street',
#     'phone': '555-555-5555',
#     'email': 'test@example.com'
#     }),content_type='application/json')
#     assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_detail_company_profile_permission(client, create_user, create_company_profile):
    client.logout()
    response = client.get(f'/accounts/companies/{create_company_profile.id}/')
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_update_company_profile_permission(client, create_user, create_company_profile):
    client.logout()
    response = client.patch(f'/accounts/companies/update/{create_company_profile.id}/', {'company_name': 'Updated Company'})
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_delete_company_profile_permission(client, create_user, create_company_profile):
    client.logout()
    response = client.delete(f'/accounts/companies/delete/{create_company_profile.id}/')
    assert response.status_code == status.HTTP_403_FORBIDDEN
