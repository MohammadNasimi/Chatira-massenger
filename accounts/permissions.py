from rest_framework.permissions import BasePermission ,SAFE_METHODS
class profile_permissions(BasePermission):
    def has_object_permission(self, request, view, obj):
            return obj.user == request.user
class user_meta_permissions(BasePermission):
    def has_object_permission(self, request, view, obj):
            return obj.profile.user == request.user