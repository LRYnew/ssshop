from django.http import Http404
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .serializers import GoodsListSerializers
from .filters import GoodsFilter


# Create your views here.


class LargeResultsSetPagination(PageNumberPagination):
    """
    分页设置
    """
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max10000_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsListSerializers
    pagination_class = LargeResultsSetPagination
    # filter_fields = ('name', 'shop_price')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ['name', 'goods_sn', 'goods_desc', 'goods_brief']
    ordering_fields = ('name', 'sold_num', 'add_time', 'update_time')
    ordering = ('name',)
