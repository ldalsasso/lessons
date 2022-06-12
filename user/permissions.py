from rest_framework import permissions


class PermissionForUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
            return True
        if view.action == 'list' and not user.is_superuser:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method == 'POST':
            return True
        if user.is_superuser:
            return True
        if obj == user:
            return True
        return False
