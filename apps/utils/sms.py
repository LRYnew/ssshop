# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 0021 11:11
# @Author  : YJob
import requests
import json


class SMS(object):
    """
    短信发送
    """

    def __init__(self, apikey):
        self.apikey = apikey
        self.sms_url = 'http://dingxin.market.alicloudapi.com/dx/sendSms'

    def sms_send(self, code, mobile):
        headers = {
            "Authorization": "APPCODE " + self.apikey
        }
        data = {
            "mobile": mobile,
            "param": 'code:' + code,
            "tpl_id": 'TP1711063'
        }

        response = requests.post(self.sms_url, headers=headers, data=data)
        re_dict = json.loads(response.text)

        return re_dict


# if __name__ == "__main__":
#     sms = SMS("efba415eab9346a98cc634531d3a3c09")
#     sms.sms_send("2018", "18876330709")
