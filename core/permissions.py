from rest_framework import permissions


class EhSuperUserDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_super_user:
                return True
            return False
        return True


class EhSuperUserPut(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            if request.user.is_super_user:
                return True
            return False
        return True


class EhSuperUserPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            if request.user.is_super_user:
                return True
            return False
        return True
