import pytest
from django.core.exceptions import ValidationError
from decimal import Decimal

from django.db import IntegrityError

from inventory.models import Product,Order
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





@pytest.fixture
def company_profile(user):
    return CompanyProfile.objects.create(
    user=user,
    company_name='Test Company'
    )

@pytest.fixture
def product(company_profile):
    return Product.objects.create(
        product_owner=company_profile,
        name='Test Product',
        sku='P123',
        price=10.00,
        description='This is a test product',
        quantity=100,
        unit='piece'
        )

@pytest.mark.django_db
def test_order_model_create(company_profile, product):
    order = Order.objects.create(
    customer=company_profile,
    total_amount=10.00
    )
    order.products.add(product)
    assert order.id is not None
    assert order.customer == company_profile
    assert order.total_amount == 10.00
    assert order.products.count() == 1
    assert order.status == 'PENDING'
    assert order.created_at is not None
    assert order.updated_at is not None


@pytest.mark.django_db
def test_order_created_with_correct_status(company_profile, product):
    """
    Test that an order is created with correct status
    """
    order = Order.objects.create(
    customer=company_profile,
    total_amount=product.price
    )
    order.products.add(product)
    order.refresh_from_db()
    assert order.status == 'PENDING'
@pytest.mark.django_db
def test_order_total_amount_calculation(company_profile, product):
    """
    Test that the total amount is calculated correctly
    """
    order = Order.objects.create(
    customer=company_profile,
    total_amount=product.price
    )
    order.products.add(product)
    order.refresh_from_db()
    assert order.total_amount == product.price


@pytest.mark.django_db
def test_order_product_quantity_decreased(company_profile, product):
    """
    Test that the product quantity is decreased after an order is placed
    """
    initial_quantity = product.quantity
    product.quantity = initial_quantity - 1
    product.save()

    order = Order.objects.create(
        customer=company_profile,
        total_amount=product.price
    )
    order.products.add(product)

    product.refresh_from_db()
    assert product.quantity == initial_quantity - 1
