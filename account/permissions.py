from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from account.models import CompanyProfile

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # return not request.user.is_authenticated

         if  request.user.is_authenticated:

                raise PermissionDenied('Authenticated User cannot create an account.')
         return True

class IsCompanyProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if  isinstance(obj, CompanyProfile):
            return obj.user == request.user
        else:
            raise PermissionDenied('You do not have permission to perform this action')