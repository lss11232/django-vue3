# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/6/1 001 23:05
@Remark: 系统管理的路由文件
"""
from django.urls import path,include
from rest_framework import routers

from dvadmin.system.views.api_white_list import ApiWhiteListViewSet
from dvadmin.system.views.user import UserViewSet
from dvadmin.system.views.menu import MenuViewSet


system_url = routers.SimpleRouter()
system_url.register(r'user', UserViewSet)
system_url.register(r'api_white_list', ApiWhiteListViewSet)


urlpatterns = [
    path('user/user_info/', UserViewSet.as_view({'get': 'user_info', 'put': 'update_user_info'})),
    path('menu/web_router/', MenuViewSet.as_view({'get': 'web_router'})),
    path('user/change_password/<int:pk>/', UserViewSet.as_view({'put': 'change_password'})),
    path('user/reset_password/<int:pk>/', UserViewSet.as_view({'put': 'reset_password'})),
    path('user/export/', UserViewSet.as_view({'post': 'export_data', })),
    path('user/import/', UserViewSet.as_view({'get': 'import_data', 'post': 'import_data'})),

]
urlpatterns += system_url.urls
