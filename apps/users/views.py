from random import choice

from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from .serializers import SmsSerializer
from utils.sms import SMS
from mxshop.settings import SMS_APPKEY
from .models import VerifyCode
# Create your views here.

User = get_user_model()


class CustomBackends(ModelBackend):
    """
    重写登录
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    短信验证码发送
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        code = self.generate_code()

        sms = SMS(SMS_APPKEY)
        sms_status = sms.sms_send(code=code, mobile=mobile)
        if sms_status['return_code'] != "00000":
            return Response({
                "mobile": sms_status.return_code
            },status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            },status=status.HTTP_201_CREATED)

        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
