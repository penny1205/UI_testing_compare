# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class PaymentDetailGet(object):
    ''' 
    支付查询页面---支付详情查询
    /api/tms/pay/getPay 
    '''
    __slots__ = ('__paymentDetailGetApiUrl', '__head_dict')
    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__paymentDetailGetApiUrl = 'https://{0}:{1}{2}/api/tms/pay/getPay'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def payment_detail_get(self, wayBillId):
        try:
            payload = {
                'wayBillId': wayBillId   # 运单主键
            }
            response = HttpClient().get(self.__paymentDetailGetApiUrl, self.__head_dict, payload)
            return response
        except Exception as e:
            Log().error('支付详情接口调用异常:{0}'.format(e))
            return None

if __name__ == '__main__':
    test = PaymentDetailGet()
    a = test.payment_detail_get('77364').json()
    print(a)