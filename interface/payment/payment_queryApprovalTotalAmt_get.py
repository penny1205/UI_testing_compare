# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class QueryApprovalTotalAmtGet(object):
    """ 查询出当日未从可借款金额中扣除的贷款总额
    [/api/tms/pay/queryApprovalTotalAmt][GET]"""

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__getQueryApprovalTotalAmtApiUrl = "https://{0}:{1}{2}/api/tms/pay/queryApprovalTotalAmt".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def queryapprovaltotalamt_get(self):
        try:
            response = HttpClient().get(self.__getQueryApprovalTotalAmtApiUrl, self.__head_dict)
            return response
        except Exception:
            return None

if __name__ == '__main__':
    test = QueryApprovalTotalAmtGet().queryapprovaltotalamt_get()
    print(test.json())
