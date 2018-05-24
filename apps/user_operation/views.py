from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserFav
from .serializers import UserFavSerializer
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# Create your views here.

class UserFavViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户商品收藏
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    # 登录验证方式
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 接口需要验证登录
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 设置 url 搜索字段
    lookup_field = 'goods_id'

    # 增加 获取收藏列表需根据用户进行获取
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)
