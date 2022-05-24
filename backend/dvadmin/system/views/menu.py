# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.decorators import action

from dvadmin.system.models import Menu, MenuButton, Button
from dvadmin.utils.json_response import SuccessResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet

from json import loads, dumps


class MenuSerializer(CustomModelSerializer):
    """
    菜单表的简单序列化器
    """
    menuPermission = serializers.SerializerMethodField(read_only=True)

    def get_menuPermission(self, instance):
        queryset = MenuButton.objects.filter(menu=instance.id).order_by('-name').values_list('name', flat=True)
        if queryset:
            return queryset
        else:
            return None

    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ["id"]


class MenuCreateSerializer(CustomModelSerializer):
    """
    菜单表的创建序列化器
    """
    name = serializers.CharField(required=False)

    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ["id"]


class WebRouterSerializer(CustomModelSerializer):
    """
    前端菜单路由的简单序列化器
    """
    path = serializers.CharField(source="web_path")
    title = serializers.CharField(source="name")
    menuPermission = serializers.SerializerMethodField(read_only=True)

    def get_menuPermission(self, instance):
        # 判断是否是超级管理员
        if self.request.user.is_superuser:
            return Button.objects.values_list('value', flat=True)
        else:
            # 根据当前角色获取权限按钮id集合
            permissionIds = self.request.user.role.values_list('permission', flat=True)
            queryset = MenuButton.objects.filter(id__in=permissionIds, menu=instance.id).values_list('value', flat=True)
            if queryset:
                return queryset
            else:
                return None

    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ["id"]


# 返回菜单信息处理
def menu_merge(data):
    data = loads(dumps(data, default=str))
    children_list = []
    merge_list = []
    # 根据 sort 的值排序
    menu_list = sorted(data, key=lambda obj: obj.get('sort'))
    # None 会在最前面
    # menu_list = sorted(menu_list, key=lambda obj: obj.get('parent'))
    # print(menu_list)
    for i in menu_list:
        if i.get('parent') is None:
            merge_list.append(
                {"id": i.get('id'), "authName": i.get('name'), "path": "", "sort": i.get('sort'),
                 "parent": i.get('parent'),
                 "children": []})
        else:
            children_list.append(i)
            # print(children_list)

    for children in children_list:
        for parent in merge_list:
            if children.get('parent') == parent.get('id'):
                parent.get('children').append({"id": children.get('id'), "authName": children.get('name'),
                                               "path": children.get('path'), "sort": children.get('sort'),
                                               "parent": children.get('parent'), "children": []})
    # print(merge_list)
    return merge_list


class MenuViewSet(CustomModelViewSet):
    """
    菜单管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    create_serializer_class = MenuCreateSerializer
    update_serializer_class = MenuCreateSerializer
    search_fields = ['name', 'status']
    filter_fields = ['parent', 'name', 'status', 'is_link', 'visible', 'cache', 'is_catalog']
    extra_filter_backends = []

    @action(methods=['GET'], detail=True, permission_classes=[])
    def web_router(self, request):
        """用于前端获取当前角色的路由"""
        # print(request)
        user = request.user
        # print(type(user))
        queryset = self.queryset.filter(status=1)
        if not user.is_superuser:
            # 用户对角色 、角色对菜单
            menuIds = user.role.values_list('menu__id', flat=True)
            # print(menuIds)
            queryset = Menu.objects.filter(id__in=menuIds, status=1)
        serializer = WebRouterSerializer(queryset, many=True, request=request)
        data = serializer.data
        #  star ****
        data = menu_merge(data)
        # end ***
        return SuccessResponse(data=data, total=len(data), msg="获取成功")
