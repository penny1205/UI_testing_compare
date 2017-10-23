# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class PaymentPayDetailGet(object):
    """ ---发车支付页面、到达支付页面、尾款支付页面---支付详情查询
     [/api/tms/pay/getPayDetail][POST] """

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__getPayDetailApiUrl = "https://{0}:{1}{2}/api/tms/pay/getPayDetail".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def payment_detail_get(self, wayBillID):
        try:
            payload = {
                "wayBillId": wayBillID   # 运单id
            }
            response = HttpClient().get(self.__getPayDetailApiUrl, self.__head_dict, payload)
            return response
        except Exception:
            return None

if __name__ == '__main__':
    test = PaymentPayDetailGet()
    a = test.payment_detail_get("77364")
    print(a)
