from rest_framework.permissions import BasePermission
from rolepermissions.checkers import has_permission


class IsHR(BasePermission):
    def has_permission(self, request, view):
        return has_permission(request.user, 'edit_employee')


class CanViewSensitiveData(BasePermission):
    def has_permission(self, request, view):
        return has_permission(request.user, 'view_sensitive_data')
