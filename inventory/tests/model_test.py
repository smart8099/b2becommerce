import pytest
from django.core.exceptions import ValidationError
from decimal import Decimal

from django.db import IntegrityError

from inventory.models import Product
from account.models import CompanyProfile
from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create_user(username='test_user')

@pytest.fixture
def company_profile(user):
    return CompanyProfile.objects.create(user=user)


@pytest.mark.django_db
def test_product_model(company_profile):
    product = Product.objects.create(
        product_owner=company_profile,
        name='Test Product',
        sku='123456',
        price=Decimal('10.99'),
        description='This is a test product',
        quantity=5,
        unit='Each'
    )
    assert product.name == 'Test Product'
    assert product.sku == '123456'
    assert product.price == Decimal('10.99')
    assert product.description == 'This is a test product'
    assert product.quantity == 5
    assert product.unit == 'Each'


@pytest.mark.django_db
def test_product_sku_unique(company_profile):
    Product.objects.create(
        product_owner=company_profile,
        name='Test Product 1',
        sku='123456',
        price=Decimal('10.99'),
        description='This is a test product',
        quantity=5,
        unit='Each'
    )
    with pytest.raises(IntegrityError) as e:
        Product.objects.create(
            product_owner=company_profile,
            name='Test Product 2',
            sku='123456',
            price=Decimal('10.99'),
            description='This is a test product',
            quantity=5,
            unit='Each'
        )
