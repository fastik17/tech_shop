from rest_framework import permissions


class IsCashierProfileOnly(permissions.BasePermission):
    """Allows access only to "is_cashier" users."""
    message = 'You must be cashier'

    def has_permission(self, request, view):
        return request.user and request.user.is_cashier


class IsSellerProfileOnly(permissions.BasePermission):
    """Allows access only to "is_seller" users."""
    message = 'You must be seller'

    def has_permission(self, request, view):
        return request.user and request.user.is_seller


class IsAccountantProfileOnly(permissions.BasePermission):
    """
    Allows access only to "is_accountant" users.
    """
    message = 'You must be accountant'

    def has_permission(self, request, view):
        return request.user and request.user.is_accountant
