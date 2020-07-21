from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import FilterSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

class MyPaination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100
# Create your views here.

class DeviceFilterSet(FilterSet):
    class Meta:
        model = models.Device
        fields = {}

class DeviceViewset(viewsets.ModelViewSet):

    pagination_class = MyPaination
   # serializer_class = serializers.UserSerializer
    queryset = models.Device.objects.all().order_by('id')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
    search_fields = ('device_id', 'device_name')
    # filter_class = UserFilterSet

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'update' or self.action == 'partial_update':
            return serializers.DeviceUpdateSerializer
        return serializers.DeviceSerializer


    def list(self, request, *args, **kwargs):
        """
        获得用户列表 
        
        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | --  | -- | -- |
        | username | 用户名 | True | str |
        | password | 密码 | True | str |
        | last_name | 昵称 | True | str|
        | email | 邮箱 | True | str |
        | tel | 电话 | True | str |
        | num | 工号 | True | str |
        | gender | 性别(1男 2女) | True | int |
        | info | 备注信息 | False | int |
        | is_active | 账户状态(1 冻结 2 激活）| False |int|


        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | 200 | 获取列表成功 | 返回数据 |
        | 400 | 参数格式错误 | 参数格式错误 |
        | 500 | 请求失败 | 服务器内部错误 |
        | 404 | 页面没有找到 | 页面没有找到 |
        """
        return super().list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        """
         新增设备

          #### 参数说明
         | 字段名称 | 描述 | 必须 | 类型 |
         | -- | -- | -- | -- |
         | username | 用户名 | True | str |
         | password | 密码 | True | str |
         | last_name | 昵称 | True | str|
         | email | 邮箱 | True | str |
         | tel | 电话 | True | str |
         | num | 工号 | True | str |
         | gender | 性别(1男 2女) | True | int |
         | info | 备注信息 | False | int |
         | is_active | 账户状态(1 冻结 2 激活）| False |int|


        #### 响应字段
         | 字段名称 | 描述 | 必须 | 类型 |
         | -- | -- | -- | -- |


         #### 响应消息：
         | Http响应码 | 原因 | 响应模型 |
         | -- | -- | -- |
         | 201 | 添加成功 | 返回数据 |
         | 400 | 参数格式错误 | 参数格式错误 |
         | 500 | 请求失败 | 服务器内部错误 |
        """
        return super().create(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):

        # id = self.kwargs.get('id')
        # try:
        #     user = models.User.objects.get(id=id)
        # except Exception as e:
        #     print(e)
        #     return Response({'msg':"找不到对象", "code":404}, status= status.HTTP_404_NOT_FOUND)

        device = self.get_object()
        device.is_active=0
        device.save()

        return Response({'msg':"", "code":200}, status= status.HTTP_200_OK)


    # /device/{id}/status
    @action(methods=['put'], detail=True, url_path='status')
    @swagger_auto_schema(request_body=serializers.DeviceUpdateStatusSerializer)
    def set_status(self, request, *args, **kwargs):

        device = self.get_object()
        is_active = self.request.data.get('is_active', 0)
        device.is_active = is_active
        device.save()

        return Response({'msg':"", "code":200}, status= status.HTTP_200_OK)

