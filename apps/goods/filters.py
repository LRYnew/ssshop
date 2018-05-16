# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 0016 17:24
# @Author  : YJob

import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类
    """
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    # icontains前面的i表示忽视大小写
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']
