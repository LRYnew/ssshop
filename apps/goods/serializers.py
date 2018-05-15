# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 0014 09:24
# @Author  : YJob
from rest_framework import serializers
from .models import Goods, GoodsCategory

class CategorySerializers(serializers.ModelSerializer):
    """
    商品分级序列化
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsListSerializers(serializers.ModelSerializer):
    """
    商品列表序列化
    """
    category = CategorySerializers()
    class Meta:
        model = Goods
        fields = '__all__'

