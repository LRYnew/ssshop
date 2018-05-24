# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 0021 11:56
# @Author  : YJob
import re
from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from mxshop.settings import regex_mobile
from .models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    """
    短信发送验证
    """
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        手机号验证
        """
        # 注册验证
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('手机已经注册过')

        # 格式验证
        if not re.match(regex_mobile, mobile):
            raise serializers.ValidationError('手机格式不符合规范')

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)

        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile):
            raise serializers.ValidationError('发送频率过高,请60s后再发送')

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户验证
    """
    # write_only 解决返回值序列化错误, 返回时不带上code
    code = serializers.CharField(write_only=True, required=True, max_length=4, min_length=4, help_text="验证码",
                                 label="验证码",
                                 error_messages={
                                     # 针对字段没上传情况 required
                                     "required": "验证码不能为空",
                                     "max_length": "验证码不能高于4位数",
                                     "min_length": "验证码不能低于4位数",
                                     "blank": "验证码不能为空"
                                 })
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, max_length=11, min_length=11,
                                     allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")])

    password = serializers.CharField(label="密码", write_only=True, style={
        'input_type': 'password'
    })

    # 创建时修改逻辑，对密码进行加密
    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    def validate_code(self, code):
        # self.initial_data 从前端传回的数据
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_code = verify_records[0]
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            print(last_code.add_time, last_code)
            if last_code.add_time < five_minutes_ago:
                raise serializers.ValidationError('验证码过期')

            if last_code.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ['username', 'mobile', 'code', 'password']
