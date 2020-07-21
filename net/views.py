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
from rest_framework_simplejwt.views import TokenObtainPairView



class MyPaination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100
# Create your views here.

class NetFilterSet(FilterSet):
    class Meta:
        model = models.Net
        fields = {}

class NetViewset(viewsets.ModelViewSet):

    pagination_class = MyPaination
    serializer_class = serializers.NetSerializer
    queryset = models.Net.objects.all().order_by('id')
   # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
   # search_fields = ('device_id', 'device_name')
    #filter_class = serializers.NetSerializer

