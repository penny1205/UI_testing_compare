#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillDriverConfirm(object):
    """  司机确认发车 [/app/payment/confirmWayBill][POST] """

    __slots__ = ('__driverConfirmWayBillApiUrl', '__head_dict', 'partnerNo')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverConfirmWayBillApiUrl = 'http://{0}:{1}{2}/payment/confirmWayBill'.format(
            config['app_api_host'], config['app_api_port'], config['app_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            # 'content-type': "application/json",
            # 'token': config['tms_api_token'],
            'YD_VERSION': '3.0',
            'YD_CLIENT': 'driver',
            'YD_OAUTH': 'eyJlbmNyeXB0ZWREYXRhIjoiTThOZ0Y3UG5LZE1KQWEzS0xOalgwVy9yNzl6S0MxSWZhTndrRitobUtrQmhtWkJIZW9BeEpwUVhMT3RKRGlhczVQNk9wdzhaQmNyRXo1RE9ZNlZoS0ZJNzNnRVJTTEZxVWk3LzAyWEZyQzBDTVpxVUlSNTFVejNVd3pXUjF1NmlFSjlCbjVqN1NxQzZBR1BmckdJTXZNSVlNT3daMGxka3JyVDczaWphck9XVUI4aEhHcUQ4VVdZMmJaMFVSdEZjT3NFaTFUQkZMMkVFeHJjTjNEZStiZU0yeUNmb202QWs1elVvUmR5Rld4SzhBNjFjQStLSUprcVp2Z1B2SEx3SiIsIndyYXBwZWRLZXkiOiJrQk9vT0U1SVp6YTdXZEsvL1F3UlFicVg5alo0OUVTNnMwZVk2djczZHdlOU1Yd1NYd3ZnZXdjUm5mL2dRNm0zdGdYUUFoMUw1cnd0NG80QWFEVnRtZz09In0='
        }

    def waybill_driver_confirm(self, billId='', partnerNo= '', totalAmt='', preAmt='', oilAmt='', destAmt='',
                                 lastAmt='', receiverId=''):
        """ 司机确认发车 """
        try:
            receipt_0 = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'logo.png'
            receipt_name_0 = os.path.basename(receipt_0)
            with open(receipt_0, 'rb') as receipt_0:
                photoAirWay = (receipt_name_0, receipt_0.read())
            payload = {'id': (None, str(billId)),
                       'partnerNo': (None, str(self.partnerNo)),
                       'totalAmt': (None, str(totalAmt)),
                       'preAmt': (None, str(preAmt)),
                       'oilAmt': (None, str(oilAmt)),
                       'destAmt': (None, str(destAmt)),
                       'lastAmt': (None, str(lastAmt)),
                       'receiverId': (None, str(receiverId)),
                       'photoAirWay': photoAirWay
                       }
            response = HttpClient().post_multipart(url=self.__driverConfirmWayBillApiUrl, files=payload,
                                                   header_dict=self.__head_dict)
            return response
        except Exception as e:
            Log().error('司机确认发车发生异常:{0}'.format(e))
            return None

if __name__ == "__main__":
    test = WayBillDriverConfirm().waybill_driver_confirm('169694', totalAmt='10', preAmt='1', oilAmt='1', destAmt='1',
                                 lastAmt='1')
    print(test.request.headers)
    print(test.request.body)
    print(test.json())
