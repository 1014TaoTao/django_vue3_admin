from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerPermission(BasePermission):
    """自定义权限"""

    def has_object_permission(self, request, view, obj):
        """判断对于指定对象Obj的操作权限"""
        if request.method == SAFE_METHODS:
            # 判断请求方式是GET/HEAD/OPTIONS安全请求，直接返回True
            return True
        # 验证操作文章对象的用户是否发表文章的用户
        return obj.user == request.user
