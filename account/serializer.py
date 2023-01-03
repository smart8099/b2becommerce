from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CompanyProfile


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class CompanyProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CompanyProfile
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(
            username=user_data["username"], password=user_data["password1"]
        )

        try:
            # Try to update the existing Company object for the User
            company = CompanyProfile.objects.get(user=user)
            for key, value in validated_data.items():
                setattr(company, key, value)
            company.save()
        except CompanyProfile.DoesNotExist:
            # Create a new Company object if one does not already exist
            company = CompanyProfile.objects.create(user=user, **validated_data)

        return company
