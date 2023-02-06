from django.urls import path, include
from .views import CreateCompanyProfileView,DeleteCompanyProfileView,DetailCompanyProfileView,UpdateCompanyProfileView


urlpatterns = [
    path("companies/create/", CreateCompanyProfileView.as_view(), name="signup"),
    path('companies/<int:id>/', DetailCompanyProfileView.as_view(), name='company-detail'),
    path('companies/update/<int:id>/', UpdateCompanyProfileView.as_view(), name='company-update'),
    path('companies/delete/<int:id>/', DeleteCompanyProfileView.as_view(), name='company-delete'),
]
