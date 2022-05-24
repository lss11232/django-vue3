# Create your views here.
from .models import PlatformModel
from .serializers import PlatformModelSerializer, PlatformModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet
from rest_framework.response import Response

from dvadmin.utils.json_response import SuccessResponse
from django.http import QueryDict
from rest_framework.request import Request
from rest_framework.authentication import BasicAuthentication


class PlatformModelViewSet(CustomModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes 为空，接口不校验权限，都可以访问此接口
    # permission_classes = []
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """

    queryset = PlatformModel.objects.all()
    serializer_class = PlatformModelSerializer
    create_serializer_class = PlatformModelCreateUpdateSerializer
    update_serializer_class = PlatformModelCreateUpdateSerializer
    filter_fields = ['platform_name', 'service_name']
    search_fields = ['platform_name']
    # 需要有 extra_filter_backends 不然报错
    extra_filter_backends = []

    # 按照  字段 去重
    def list(self, *args, **kwargs):
        if 'field' in  self.request.query_params.dict():
            field = self.request.query_params.dict().get('field')
            # field = 'platform_name'
            queryset = PlatformModel.objects.values(field).order_by(field).distinct()
            meta = { "meta": {
                "msg": "登录成功",
                "status": 200
            }}
            return SuccessResponse(queryset, msg="获取成功")
            # return Response(queryset)
        else:
            return super().list(self.request)


#
# class get_Plat(PlatformModelViewSet):
#
#     '''
#     # 获取get 或 post的参数
#     # 使用方法：get_parameter_dic(request)['name'] ,name为获取的参数名 ,此种方式获取name不存在则会报错返回name表示name不存在，需要此参数
#     # get_parameter_dic(request).get('name') ,name为获取的参数名 ,此种方式获取name不存在不会报错，不存在会返回None
#     def get_parameter_dic(request, *args, **kwargs):
#         print(request,'request')
#         # 判断  request 是不是 Request 类型
#         if isinstance(request, Request) == False:
#             return {}
#         query_params = request.query_params
#
#         if isinstance(query_params, QueryDict):
#             query_params = query_params.dict()
#         result_data = request.data
#         if isinstance(result_data, QueryDict):
#             result_data = result_data.dict()
#         if query_params != {}:
#             return query_params
#         else:
#             return result_data
#         '''
#
#
#     # ###
#     # # 按照  字段 去重
#     def list(self, *args, **kwargs):
#         if 'field' in  self.request.query_params.dict():
#             field = self.request.query_params.dict().get('field')
#             # field = 'platform_name'
#             queryset = PlatformModel.objects.values(field).order_by(field).distinct()
#             return Response(queryset)
#         else:
#             return super().list(self.request)
