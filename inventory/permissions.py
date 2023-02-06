from rest_framework import permissions
from account.models import CompanyProfile


class IsProductOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post

        user_profile = CompanyProfile.objects.get(user_id=request.user)
        return obj.product_owner == user_profile
