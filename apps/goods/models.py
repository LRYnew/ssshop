# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
    商品分类
    """
    CATEGORY_TYPE = (
        (1, '一级类目')
        (2, '二级类目')
        (3, '三级类目')
    )

    name = models.CharField(verbose_name='类别名', max_length=30, default='', help_text='类别')
    code = models.CharField(verbose_name='类别code', max_length=30, default='', help_text='类别code')
    desc = models.TextField(verbose_name='类别描述', default='', help_text='类别描述')
    category_type = models.IntegerField(verbose_name='类目级别', choices=CATEGORY_TYPE, help_text='类目级别')
    parent_category = models.ForeignKey('self', verbose_name='父类', null=True, blank=True, help_text='父类',
                                        related_name='sub_cat')
    is_tab = models.BooleanField(verbose_name='tab栏标志', default=False, help_text='父类')

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(verbose_name='品牌名', max_length=30, default='', help_text='品牌名')
    desc = models.TextField(verbose_name='品牌描述', default='', help_text='品牌描述')
    image = models.ImageField(verbose_name='照片', upload_to='brand/%Y/%m', max_length=200)

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '品牌名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类别', null=True, blank=True)
    goods_sn = models.CharField(verbose_name='商品唯一货号', max_length=50, default='')
    name = models.CharField(verbose_name='商品名', max_length=300)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    sold_nums = models.IntegerField(verbose_name='销售数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    goods_nums = models.IntegerField(verbose_name='库存数', default=0)
    market_price = models.FloatField(verbose_name='市场价', default=0)
    shop_price = models.FloatField(verbose_name='售卖价', default=0)
    goods_brief = models.TextField(verbose_name='商品简介', max_length=500)
    goods_desc = UEditorField(verbose_name=u'内容描述', imagePath='goods/images/', width=1000, height=300,
                              filePath='goods/files/', default='')
    ship_free = models.BooleanField(verbose_name='是否承担运费', default=True)
    goods_front_image = models.ImageField(verbose_name='商品图片', null=True, blank=True, upload_to='goods/front/%Y/%m',
                                          max_length=200)
    is_new = models.BooleanField(verbose_name='新品标志', default=False)
    is_hot = models.BooleanField(verbose_name='热卖标志', default=False)

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品图
    """
    goods = models.ForeignKey(Goods, verbose_name='商品', related_name='images')
    image = models.ImageField(verbose_name='商品轮播图片', upload_to='goods/brand/%Y/%m', null=True, blank=True)

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '商品图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models, models):
    """
    首页轮播
    """
    goods = models.ForeignKey(Goods, verbose_name='商品')
    image = models.ImageField(verbose_name='轮播图', upload_to='banner/%Y/%m')
    index = models.IntegerField(verbose_name='轮播顺序', default=0)

    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    add_time = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
