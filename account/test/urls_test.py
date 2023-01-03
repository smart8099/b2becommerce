import pytest
from django.contrib.auth.models import User
from account.models import CompanyProfile
from django.urls import reverse, resolve
from account.views import CreateCompanyView


def test_create_company_view():

    url = reverse("signup")
    print(url)

    assert resolve(url).func.view_class == CreateCompanyView
