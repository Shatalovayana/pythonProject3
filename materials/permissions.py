from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        elif request.user.groups.filter(name='moderator').exists():
            return True


class IsOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        elif request.user.is_staff:
            return True
        return request.user == view.get_object().owner
