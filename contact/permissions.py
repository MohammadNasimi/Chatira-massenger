from rest_framework.permissions import BasePermission ,SAFE_METHODS
class update_contact_permissions(BasePermission):
    def has_object_permission(self, request, view, obj):
            return obj.user.user == request.user