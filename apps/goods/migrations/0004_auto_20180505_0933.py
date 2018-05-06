# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180504_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_front_image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='goods/images/', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/', verbose_name='照片'),
        ),
    ]
