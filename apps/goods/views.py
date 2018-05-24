# -*- coding:utf-8 -*-
from django.http import Http404
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods, GoodsCategory
from .serializers import GoodsListSerializers, CategorySerializers
from .filters import GoodsFilter


# Create your views here.


class LargeResultsSetPagination(PageNumberPagination):
    """
    分页设置
    """
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max10000_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表, 筛选、过滤、搜索、排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsListSerializers
    pagination_class = LargeResultsSetPagination
    # filter_fields = ('name', 'shop_price')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ['name', 'goods_sn', 'goods_desc', 'goods_brief']
    ordering_fields = ('sold_num', 'shop_price')
    ordering = ('name',)


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializers
