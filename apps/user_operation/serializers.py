# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 0024 14:08
# @Author  : YJob
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    """
    用户商品收藏验证
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        # # 字段联合唯一验证 功能
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="请勿重复收藏"
            )
        ]
        fields = ['id', 'user', 'goods']
