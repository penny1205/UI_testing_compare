# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class ApprovalTotalAmtGet(object):
    '''
    获取今日借款中金额
    [/api/tms/pay/queryApprovalTotalAmt][GET]
    '''
    __slots__ = ('__approvalTotalAmtGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__approvalTotalAmtGetApiUrl = 'https://{0}:{1}{2}/api/tms/pay/queryApprovalTotalAmt'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def approval_total_amt_get(self):
        try:
            response = HttpClient().get(self.__approvalTotalAmtGetApiUrl, self.__head_dict)
            return response
        except Exception as e:
            Log().error('到达支付列表接口调用异常:{0}'.format(e))
            return None

if __name__ == '__main__':
    test = ApprovalTotalAmtGet().queryapprovaltotalamt_get()
    print(test.json())
