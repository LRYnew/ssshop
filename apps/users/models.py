# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(verbose_name='姓名', max_length=20, null=True, blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    mobile = models.CharField(verbose_name='手机', max_length=11, null=True, blank=True)
    gender = models.CharField(verbose_name='性别', max_length=6, choices=(('man', '男'), ('woman', '女')), default='man')
    email = models.EmailField(verbose_name='邮箱', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(verbose_name='手机', max_length=11)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
