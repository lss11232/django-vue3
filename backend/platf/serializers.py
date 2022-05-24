"""
  @author: lss
  @file: serializers.py
  @desc:
"""
from .models import PlatformModel
from dvadmin.utils.serializers import CustomModelSerializer


class  PlatformModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = PlatformModel
        fields = "__all__"


class  PlatformModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = PlatformModel
        fields = '__all__'
