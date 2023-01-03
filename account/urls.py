from django.urls import path, include
from .views import CreateCompanyView


urlpatterns = [path("create/", CreateCompanyView.as_view(), name="signup")]
