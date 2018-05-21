"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from django import views
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .settings import MEDIA_ROOT
import xadmin

from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewSet

# 路由
router = DefaultRouter()
# 商品路由
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 商品分类路由
router.register(r'categorys', CategoryViewSet, base_name='categorys')
# 验证码发送
router.register(r'codes', SmsCodeViewSet, base_name='codes')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls')),

    # 媒体文件路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 文档
    url(r'^docs/', include_docs_urls(title="生鲜商城")),

    url(r'^', include(router.urls)),

    # 登录
    url(r'^login/', obtain_jwt_token),
]
