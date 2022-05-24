"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin

# ---


from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from dvadmin.system.views.login import LoginView, CaptchaView, ApiLogin, LogoutView
from dvadmin.utils.swagger import CustomOpenAPISchemaGenerator
from rest_framework import permissions
# 导入 simplejwt 提供的几个验证视图类，这是drf写好的轮子，都不要自己写视图
"""
TokenObtainPairView  登录 获取tocken
TokenRefreshView     刷新的 tocken
TokenVerifyView      验证的tocken
"""
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="文档描述",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomOpenAPISchemaGenerator,

)


urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/system/', include('dvadmin.system.urls')),
    path('api/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/captcha/', CaptchaView.as_view()),
    # path('apiLogin/', ApiLogin.as_view()),
    path('', include('platf.urls'))
]





