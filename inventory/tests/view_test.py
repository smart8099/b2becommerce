import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from inventory.models import Product
from account.models import CompanyProfile
from decimal import Decimal
from inventory.serializers import ProductSerializer
import json


@pytest.fixture
def user():
    return User.objects.create_user(username='test_user')

@pytest.fixture
def company_profile(user):
    return CompanyProfile.objects.create(user=user)

@pytest.fixture
def product(company_profile):
    return Product.objects.create(
        product_owner=company_profile,
        name='Test Product',
        sku='123456',
        price=Decimal('10.99'),
        description='This is a test product',
        quantity=5,
        unit='Each'
    )


#
@pytest.mark.django_db
def test_product_create_view(client, company_profile, user):
    client.force_login(user)
    url = reverse('add-product')
    data = {'name': 'test product', 'sku': '123456', 'price': '10.99',
            'description': 'This is a test product', 'quantity': 5, 'unit': 'Each'}
    response = client.post(url, data)
    assert response.status_code == 201
    assert Product.objects.count() == 1
    assert Product.objects.get().name == 'test product'
    assert Product.objects.get().product_owner == company_profile

@pytest.mark.django_db
def test_products_list_view(client):
    url = reverse('lists-products')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == Product.objects.count()

@pytest.mark.django_db
def test_product_detail_view(client,product,user):
    client.force_login(user)
    url = reverse('product-detail', kwargs={'uuid': product.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == product.name
    assert response.data['description'] == product.description

@pytest.mark.django_db
def test_product_update_view(client,product,user):
    client.force_login(user)
    url = reverse('product-update', kwargs={'uuid': product.id})
    data = {'name': 'updated test product', 'sku': '123456', 'price': '10.99',
            'description': 'This is an updated test product', 'quantity': 5, 'unit': 'Each'}

    response = client.put(url, data, content_type='application/json')
    assert response.status_code == 200
    assert Product.objects.get().name == 'updated test product'

@pytest.mark.django_db
def test_product_delete_view(client,product,user):
    client.force_login(user)
    url = reverse('product-delete', kwargs={'uuid': product.id})
    response = client.delete(url)
    assert response.status_code == 204
    assert Product.objects.count() == 0