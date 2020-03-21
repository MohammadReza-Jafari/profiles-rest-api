from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow User to edit their profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return request.user == obj
