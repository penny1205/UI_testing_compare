#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillDriverConfirm(object):
    """  司机确认发车 [/app/payment/confirmWayBill][POST] """

    __slots__ = ('__driverConfirmWayBillApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverConfirmWayBillApiUrl = 'http://{0}:{1}{2}/payment/confirmWayBill'.format(
            config['app_api_host'], config['app_api_port'], config['app_api_path'])
        self.__head_dict = {
            # 'content-type': "application/json",
            # 'token': config['tms_api_token'],
            'YD_VERSION': '2.14',
            'YD_CLIENT': 'driver',
            'YD_OAUTH': 'eyJlbmNyeXB0ZWREYXRhIjoiQmdJd2JJSXBTd3ZGQ0YzVHFEUFR0WjNQQXN2eWk1Sk9nb2NrODB5ZHNlT3FpYkJ5ckRXbjVmWCtJUDhUZmNJRFkzSUhEeTVlNlZCeU1rdUM5UE5XeTZkREswZGpCeElXL0J4U01Kb3huN0x0TWZDRkhHYldvL1luRlU3TTQ3RklJV0J3cHVTc0Qzbm5wYzAzNDhuYUQwWG9FcHA0Tm1ZTGVVMi9iTjBDSUdGaWk2azRlMHdKSm1KNTJxT0lkaUFVMnJoU0h1NEZJVGJMNmVZMnhSclRaUGFNbFhIYzVCZk1vWk5PMSt6di9UVFJaMEFIRXE5THM3MFA4V1NVZzM3UyIsIndyYXBwZWRLZXkiOiIwVjV4SHBjM1hNM010bEhjTUhtUjhUR3dFNkFEMG1oYVVETVNOSEVhc3kzS0ErckxrdkE1VzJQcXJzNEtMQ1pKOFNRYUFYamlkUXl1dmV3YmltVnRkdz09In0=='
        }

    def waybill_driver_confirm(self, billId='', partnerNo='ShiDeTang', totalAmt='', preAmt='', oilAmt='', destAmt='',
                                 lastAmt='', receiverId=''):
        """ 司机确认发车 """
        try:
            receipt_0 = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'logo.png'
            receipt_name_0 = os.path.basename(receipt_0)
            with open(receipt_0, 'rb') as receipt_0:
                photoAirWay = (receipt_name_0, receipt_0)
            payload = {'id': (None, str(billId)),
                        'partnerNo': (None, str(partnerNo)),
                        'totalAmt': (None, str(totalAmt)),
                        'preAmt': (None, str(preAmt)),
                        'oilAmt': (None, str(oilAmt)),
                        'destAmt': (None, str(destAmt)),
                        'lastAmt': (None, str(lastAmt)),
                        'receiverId': (None, str(receiverId)),
                        'photoAirWay': photoAirWay,
                       }
            response = HttpClient().post_multipart(self.__driverConfirmWayBillApiUrl, payload, self.__head_dict)
            return response
        except Exception:
            return None

if __name__ == "__main__":
    test = WayBillDriverConfirm().waybill_driver_confirm('77733', totalAmt='10', preAmt='1', oilAmt='1', destAmt='1',
                                 lastAmt='1')
    print(test.request.headers)
    print(test.request.body)
    print(test.json())
