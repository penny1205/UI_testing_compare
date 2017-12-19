# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class DefinedFeeUpdate(object):
    '''
     更新自定义费用
    [api/tms/pay/updateUserDefinedFee][POST]
    '''
    __slots__ = ('__definedFeeUpdateApiUrl', '__head_dict')
    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__definedFeeUpdateApiUrl = 'https://{0}:{1}{2}/api/tms/pay/updateUserDefinedFee'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def defined_fee_update(self, wayBillId, handlingFee=0, deliveryFee=0, oilCardDeposit=0, otherFee=0):
        try:
            payload = {
                'wayBillId': wayBillId,             # 运单ID，int，必填字段；
                'handlingFee': handlingFee,         # 装卸费，非必填(自动转换为0)，两位小数的正数；
                'deliveryFee': deliveryFee,         # 送货费，非必填(自动转换为0)，两位小数的正数；
                'oilCardDeposit': oilCardDeposit,   # 油卡金额，非必填(自动转换为0)，两位小数的正数；
                'otherFee': otherFee                # 其他费用，非必填(自动转换为0)，两位小数的正数；
            }
            response = HttpClient().post_json(self.__definedFeeUpdateApiUrl,
                                              header_dict=self.__head_dict, body_dict=payload, param_dict=payload)
            return response
        except Exception as e:
            Log().error('更新自定义费用接口调用异常:{0}'.format(e))
            return None

if __name__ == '__main__':
    test = DefinedFeeUpdate().defined_fee_update('77934', handlingFee=10, deliveryFee=10, oilCardDeposit=10, otherFee=10)
    print(test.json())
