# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class PaymentBatches(object):
    '''
    批量支付
    [api/tms/pay/batche][POST]
    '''
    __slots__ = ('__paymentBatchesApiUrl', '__head_dict')
    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__paymentBatchesApiUrl = 'https://{0}:{1}{2}/api/tms/pay/batche'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def payment_batches(self, wayBillIds, paymentMethod=None, amountType=None, amount='', password='', verifiCode=''):
        try:
            payload = {
                'wayBillIds': wayBillIds,        # 运单ID(String)数组，以逗号间隔，如 '123,456,789'
                'paymentMethod': paymentMethod,  # 支付方式，int【贷款付商户=1】、【余额付司机=2】、【白条付司机=3】、【线下支付=4】
                'amountType': amountType,        # 预付款1，油卡2，到付款3，尾款4
                'amount': amount,                # 实际支付金额，double
                'password': password,            # 使用线下支付时必填，其他不填；
                'verifiCode': verifiCode,        # 可能会有，非必填
            }
            response = HttpClient().post_json(self.__paymentBatchesApiUrl, header_dict=self.__head_dict,
                                              body_dict=payload, param_dict=payload)
            return response
        except Exception as e:
            Log().error('批量支付接口调用异常:{0}'.format(e))
            return None

if __name__ == '__main__':
    test = PaymentBatches()
    a = test.payment_batches('22893,22857', '4', '1', '10')
    print(a.json())
