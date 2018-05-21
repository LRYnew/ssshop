# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 0021 11:56
# @Author  : YJob
import re
from datetime import datetime, timedelta
from rest_framework import serializers
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

