from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from student import views as student_view

schema_view = get_schema_view(
    openapi.Info(
        title="Lemon API接口文档平台",
        default_version='v1',
        description="这是一个美轮美奂的接口文档",
        terms_of_service="http://api.keyou.site",
        contact=openapi.Contact(email="948080782@qq.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

# 挂载注册视图集
router.register(r'students', student_view.StudentViewSet, basename='students')

urlpatterns = [
    # 对测试人员更友好
    re_path(r'^$', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    # 对开发人员更友好
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # 添加身份认证管理子路由
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))

]
