import pytest
from django.urls import reverse
from account.views import CreateCompanyView
from django.contrib.auth.models import User
from account.models import CompanyProfile
import json

companies_url = "http://127.0.0.1:8000/accounts/create/"


@pytest.fixture
def app_urls():
    return "account.urls"


def test_create_company_profile_without_argument_should_fail(client) -> None:
    response = client.post(path=reverse("signup"))
    assert response.status_code == 400


# @pytest.mark.django_db
# def test_create_company_view(client,app_urls):
#     # create a user to associate with the company
#     user = User.objects.create_user(
#     username='testuser',
#     password='testpass',
#     email='test@example.com'
#     )
#
#     # create company data to POST to the view
#     company_data = {
#         'user': user.id,
#         'company_name': 'Test Company',
#         'industry_type': 'MAN',
#         'tax_identification_number': '1234567890',
#         'address_one': '123 Test St',
#         'phone': '123-456-7890',
#         'email': 'test@example.com'
#     }
#
#     #     user=user,
#     #     company_name='Test Company',
#     #     industry_type=CompanyProfile.IndustryType.IT,
#     #     tax_identification_number='123456',
#     #     address_one='123 Main St',
#     #     phone='555-555-5555',
#     #     email='company@example.com'
#     # )
#
#     print(reverse('signup'))
#     # send a POST request to the view with the company data
#     response = client.post(companies_url, data=company_data)
#     print(response.status_code)
#
#     # assert that the request was successful and the company was created
#     assert response.status_code == 201
#     assert CompanyProfile.objects.count() == 1
#     company = CompanyProfile.objects.first()
#     assert company.user == user
#     assert company.company_name == 'Test Company'
#     assert company.industry_type == 'MAN'
#     assert company.tax_identification_number == '1234567890'
#     assert company.address_one == '123 Test St'
#     assert company.phone == '123-456-7890'
#     assert company.email == 'test@example.com'
