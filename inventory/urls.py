from django.urls import path, include
from .views import ProductViewSet,ProductsList, ProductDetailView,ProductDeleteView,ProductUpdateView,OrderCreateAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
urlpatterns = [
    # path("", include(router.urls)),

    path('products-lists/',ProductsList.as_view(), name='lists-products'),
    path("products/add/", ProductViewSet.as_view(), name="add-product"),
    path('products/<str:uuid>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/delete/<str:uuid>/', ProductDeleteView.as_view(), name='product-delete'),
    path('products/update/<str:uuid>/', ProductUpdateView.as_view(), name='product-update'),
    path('orders/',OrderCreateAPIView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
