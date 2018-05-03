# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
# from users.models import UserProfile 以上代替

from goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    goods_num = models.IntegerField(verbose_name='商品数量', default=0)

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("unpaid", "待支付"),
    )

    user = models.ForeignKey(User, verbose_name='用户')
    order_sn = models.CharField(verbose_name='订单号', unique=True, max_length=30)
    trade_no = models.CharField(verbose_name='支付宝订单号', max_length=100, unique=True, null=True, blank=True)
    pay_status = models.CharField(verbose_name='订单支付状态', choices=ORDER_STATUS, max_length=20)
    post_script = models.CharField(verbose_name='订单留言', max_length=200)
    order_mount = models.FloatField(verbose_name='订单金额', default=0.0)
    pay_time = models.DateTimeField(verbose_name='支付时间', null=True, blank=True)

    address = models.CharField(verbose_name='收货地址', max_length=100, default='')
    signer_name = models.CharField(verbose_name='签收人', max_length=20, default='')
    signer_mobile = models.CharField(verbose_name='联系电话', max_length=11, )

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单商品详情
    """
    order = models.ForeignKey(OrderInfo, verbose_name='订单')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    goods_num = models.ForeignKey(verbose_name='商品数量', default=0)

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
